#!/usr/bin/env python

# Submit jobs to prepare datacards and run limits.
# A job is submitted per process and signal region.
# Jobs run on condor.

import os,sys
from string import *

# Date to label the job set.
date = sys.argv[1]

# Physics models
models = ['T6ttZH']

# List of SRs for which to run limits.  
# Modify the SR list as needed.
# Individual SRs option - given as list:
allSRs = ['SR_Had_1htop',
      'SR_Had_2htop',
      'SR_Had_V_b_45j',
      'SR_Had_V_b_6j',
      'SR_Had_1V_0b_34j',
      'SR_Had_1V_0b_5j',
      'SR_Had_2V_0b_24j',
      'SR_Had_2V_0b_5j',
      'SR_Had_H_b_45j',
      'SR_Had_H_b_6j',
      #SR_Had_2H_b_6j,
      'SR_Had_HV_b_6j',
      'SR_Had_H_0b_34j',
      'SR_Had_H_0b_5j',
      #SR_Had_2H_0b_34j,
      #SR_Had_2H_0b_5j,
      'SR_Had_HV_0b_24j',
      'SR_Had_HV_0b_5j',
    # Isolated lepton signal regions
      'SR_Lep_1htop',
      'SR_Lep_V_b',
      'SR_Lep_V_0b',
      'SR_Lep_H_b',
      'SR_Lep_H_0b',
    # Non-isolated lepton signal regions
      'SR_Leptop_0htop',
      'SR_Leptop_1htop',
      'SR_Lepjet_0V_24j',
      'SR_Lepjet_0V_5j',
      'SR_Lepjet_1V_24j',
      'SR_Lepjet_1V_5j',
]

# Filter region sublists:
hadSRs = filter(lambda sr: '_Had_' in sr, allSRs)
lepSRs = filter(lambda sr: '_Lep_' in sr, allSRs)
HSRs = filter(lambda sr: 'd_H' in sr or 'p_H' in sr, allSRs)
VSRs = filter(lambda sr: 'V' in sr, allSRs)
topSRs = filter(lambda sr: 'top' in sr, allSRs)
LeptopSRs = filter(lambda sr: 'Leptop' in sr, allSRs)
LepjetSRs = filter(lambda sr: 'Lepjet' in sr, allSRs)
nisolepSRs = filter(lambda sr: 'Leptop' in sr or 'Lepjet' in sr, allSRs)

# Dictionary option - specify regions list name (e.g. had) and list of regions: 
SRs = {'all' : allSRs}
SRs = {'had' : hadSRs,
       'lep' : lepSRs,
       'H' : HSRs,
       'V' : VSRs,
       'top' : topSRs,
       'nisolep' : nisolepSRs,
       'Leptop' : LeptopSRs,
       'Lepjet' : LepjetSRs}

SRs = {'had' : hadSRs,
       'lep' : lepSRs
      }

# Limit code directory
# Modify path below to match your setup:
maindir = '/afs/cern.ch/user/s/ssekmen/work/RazorRun2/limit/razorlimits/'
# Datacard making script
dcscr = maindir+'makedatacards_rzr.py'
# Limit running script templates:
lmscrtmp = 'temps/runlimits_rzr_temp.py'
lmscrtmpcnt = open(lmscrtmp).read()
lmruntmp = 'temps/rundclimits_temp.sh'
lmruntmpcnt = open(lmruntmp).read()

# Condor submission script template.  See below link for details:
# https://batchdocs.web.cern.ch/local/submit.html
cndtmpcnt = '''
executable            = exename.sh
arguments             = $(ClusterId) $(ProcId)
output                = exename.$(ClusterId).$(ProcId).out
error                 = exename.$(ClusterId).$(ProcId).out
log                   = exename.$(ClusterId).log
+JobFlavour           = "tomorrow"
queue
'''

# Loop over the models and regions / region groups:
for m in models:
    for sr in SRs:
        if type(SRs) is dict:
            srlist = SRs[sr]
            print(sr, srlist)
            srlisttxt = ' '.join(srlist)
        else: srlisttxt = sr
        # datacard preparation
        dccommand = 'python3 %s --date %s --model %s --regslist %s --regsname %s --fresh False' % (dcscr, date, m, srlisttxt, sr)
        # running limits
        if sr == 'all' : sr = ''
        if len(sr) > 0: sr = '_'+sr
        print sr
        dname = maindir+'runs/run_'+m+sr+'/'
	if not os.path.exists(dname):
            #os.mkdir(dname)
            os.system('mkdir -p '+dname)
        os.chdir(dname)
        lmscrn = 'rundclimits_'+m+sr+'.py'
        lmscrcnt = lmscrtmpcnt
        lmscrcnt = lmscrcnt.replace('dirextname', sr)
        lmscrcnt = lmscrcnt.replace('modelname', m)
        lmscrcnt = lmscrcnt.replace('datename', date)
        flmscr = open(lmscrn, "w")
        flmscr.write(lmscrcnt)
        lmrunn = 'rundclimits_'+m+sr+'.sh'
        lmruncnt = lmruntmpcnt
        lmruncnt = lmruncnt.replace('dccommand', dccommand)
        lmruncnt = lmruncnt.replace('scriptname', lmscrn)
        lmruncnt = lmruncnt.replace('dirname', dname)
        flmrun = open(lmrunn, "w")
        flmrun.write(lmruncnt)
        flmrun.close()
        cmd = 'chmod +x '+lmrunn
        cndn = 'rundclimits_'+m+sr+'.job'
        cndcnt = cndtmpcnt
        cndcnt = cndcnt.replace('exename', 'rundclimits_'+m+sr)
        fcnd = open(cndn, "w")
        fcnd.write(cndcnt)
        fcnd.close()
        print cmd
        os.system(cmd)
        print os.getcwd()
        cmd = 'condor_submit '+cndn
        print cmd
        os.system(cmd)
    break
