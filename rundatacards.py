#!/usr/bin/env python

# Produce datacards for a model and a list of regions.

import os,sys
from string import *
import argparse

# Date to label the job set.
date = sys.argv[1]

# Physics models
models = ['R2bbqqlv']
models = ['R5ttbl']
models = ['TChiWW']
models = ['TChiWZ']

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


SRs = {'V' : VSRs,
       'nisolep' : nisolepSRs, 
       'Leptop' : LeptopSRs, 
       'Lepjet' : LepjetSRs}

SRs = {'V' : VSRs}


print(SRs)


dcscr = 'makedatacards_rzr.py'

# Loop over the models and regions / region groups:
for m in models:
    for sr in SRs:
        if type(SRs) is dict:
            srlist = SRs[sr]
            print(sr, srlist)
            srlisttxt = ' '.join(srlist)
        else: srlisttxt = sr
        print(srlisttxt)
        # datacard preparation
        cmd = 'python3 %s --date %s --model %s --regslist %s --regsname %s --fresh False' % (dcscr, date, m, srlisttxt, sr)
        print cmd
        os.system(cmd)

