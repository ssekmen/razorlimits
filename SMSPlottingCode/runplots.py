#!/usr/bin/env python

import os,sys
from string import *

date = sys.argv[1]

# Medels to plot
models = ['T6ttZH']

# Regions to plot - provide regions / region sets of interest in a list
SRs = ['SR_Had_1htop',
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

SRs = ['', 'lep', 'had', 'top', 'Lepjet', 'Leptop', 'V', 'H']


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
