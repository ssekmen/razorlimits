#!/usr/bin/env python

import os,sys
from string import *

date = sys.argv[1]
models = ['T6ttZH']
models = ['TChiWW', 'TChiWZ', 'T5bbbbZH', 'T5qqqqWH', 'T5ttcc', 'T6ttZH', 'R2bbqqlv', 'R5ttbl']
models = ['TChiWW', 'TChiWZ', 'T5bbbbZH', 'T5ttcc', 'T6ttZH']
#models = ['R2bbqqlv', 'R5ttbl']
models = ['T5ttcc', 'TChiWZ', 'TChiWW', 'T6ttZH']
models = ['T5bbbbZH', 'T5qqqqWH']

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


SRs = ['all', 'had', 'lep', 'H', 'V', 'top', 'nisolep', 'Lepjet', 'Leptop']
SRs = ['all', 'had', 'lep', 'V', 'top', 'nisolep', 'Lepjet', 'Leptop']
SRs = ['lep', 'nisolep', 'top', 'Lepjet', 'Leptop']

# Contour calculating script
scr = 'Get2DContour.py'

# Loop over the processes and ctaus:
for m in models:
    for s in SRs:
        cmd = 'python %s %s %s %s' % (scr, m, s, date)
        print cmd
        os.system(cmd)



