#!/usr/bin/env python

import os,sys
from string import *

date = sys.argv[1]

# Medels to plot
models = ['T6ttZH']
models = ['TChiWW', 'TChiWZ', 'T5bbbbZH', 'T5ttcc', 'T6ttZH', 'R2bbqqlv', 'R5ttbl']
models = ['TChiWW', 'TChiWZ', 'T5bbbbZH', 'T5ttcc', 'T6ttZH']
models = ['TChiWW', 'TChiWZ', 'T6ttZH', 'T5ttcc']
models = ['TChiWZ', 'TChiWW', 'T5ttcc', 'T6ttZH', 'T5qqqqWH', 'T5bbbbZH', 'R2bbqqlv']
models = ['R5ttbl']

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
VSRs = filter(lambda sr: 'V' in sr and not '0V' in sr, allSRs)
topSRs = filter(lambda sr: 'top' in sr and not '0htop' in sr, allSRs)
LeptopSRs = filter(lambda sr: 'Leptop' in sr, allSRs)
LepjetSRs = filter(lambda sr: 'Lepjet' in sr, allSRs)
nisolepSRs = filter(lambda sr: 'Leptop' in sr or 'Lepjet' in sr, allSRs)

# Dictionary option - specify regions list name (e.g. had) and list of regions: 
SRs = {'all' : allSRs,
       'had' : hadSRs,
       'lep' : lepSRs,
       'H' : HSRs,
       'V' : VSRs,
       'top' : topSRs,
       'nisolep' : nisolepSRs,
       'Leptop' : LeptopSRs,
       'Lepjet' : LepjetSRs}
#SRs = {'all' : allSRs}

SRs = ['', 'had', 'lep', 'H', 'V', 'top', 'Lepjet', 'Leptop', 'nisolep']

#SRs = ['lep']

if not os.path.exists(date):
    os.mkdir(date)

# Loop over the processes and run the final plots:
for m in models:
    cfgtmp = open('config/Razor/templates/%s_Rzr_exp_temp.cfg' % m).read()
    print cfgtmp
    for sr in SRs:
        if len(sr) > 0: sr = '_'+sr
        fname = '../limits2root/%s/%s%s/results/%s_Rzr_results.root' % (date, m, sr, m)
        print 'Trying... '+fname
        if os.path.exists(fname):
            # copy result file 
            cmd = 'cp '+fname+' syst_results/Razor/results/%s_Rzr_results.root' % (m)
            print cmd
            os.system(cmd)
            # write the plotting cfg file for bin
            cfgf = open(('config/Razor/%s_Rzr%s_exp.cfg' % (m, sr)), "w")
            cfgf.write(cfgtmp)
            cfgf.write('BOXES Razor '+sr[1:])
            cfgf.close()
            # run plotter
            cmd = 'python scripts/makeSMSplots.py config/Razor/%s_Rzr%s_exp.cfg %s %s %s' % (m, sr, m, date, sr[1:]+'_' )
            print cmd
            os.system(cmd)

            os.system('mv *%s.* %s/' % (date, date))
#            break
