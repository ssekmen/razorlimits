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
      #'SR_Leptop_0htop', # 'SR_Leptop_0htop',
      'SR_Lepjet_1htop', # 'SR_Leptop_1htop',
      'SR_Lepjet_0V_24j',
      'SR_Lepjet_0V_5j',
      'SR_Lepjet_1V_24j',
      'SR_Lepjet_1V_5j',
]

# Filter region sublists:
hadSRs = filter(lambda sr: '_Had_' in sr, allSRs)
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


SRs = allSRs

SRs = {'all' : allSRs}


#SRs = ['SR_Had_1V_0b_34j']

print(SRs)

dcscr = 'drawsyst.py'


# Systematics
syst1 = [
    "_topptUp",
    "_topptDown",
    "_isrUp",
    "_isrDown",
    "_pileupUp",
    "_pileupDown",
    "_L1PreFiringUp",
    "_L1PreFiringDown",
    "_alphasUp",
    "_alphasDown",
    "_scaleUp",
    "_scaleDown",
]

syst2 = [
    "_lostlepUp",
    "_lostlepDown",
    "_triggerUp",
    "_triggerDown",
    "_jesUp",
    "_jesDown",
    "_jerUp",
    "_jerDown",
    "_puidUp",
    "_puidDown",
]

syst3 = [
    "_EleFullsimUp",
    "_EleFullsimDown",
    "_EleFastsimUp",
    "_EleFastsimDown",
    "_MuonFullsimUp",
    "_MuonFullsimDown",
    "_MuonFastsimUp",
    "_MuonFastsimDown",
    "_BTagUp",
    "_BTagDown",
    "_BTagFastsimUp",
    "_BTagFastsimDown",
]    

syst4 = [
    "_cf_QTWUp",
    "_cf_QTWDown",
    "_cf_ZUp",
    "_cf_ZDown",
    "_cf_NonIso_Up",
    "_cf_NonIso_Down",
    "_BoostTagUp",
    "_BoostTagDown",
    "_BoostTag_FastsimUp",
    "_BoostTag_FastsimDown",
    "_BoostmisTagUp",
    "_BoostmisTagDown",
]

systlists = {
    "syst1" : syst1,
    "syst2" : syst2,
    "syst3" : syst3,
    "syst4" : syst4,
}

years = ['run2', '2016', '2017', '2018']

# Loop over the models and regions / region groups:
for m in models:
    for sr in SRs:
        if type(SRs) is dict:
            srlist = SRs[sr]
            print(sr, srlist)
            srlisttxt = ' '.join(srlist)
        else: srlisttxt = sr
        print(srlisttxt)
        for year in years:
            for syst in systlists:
                systtxt = ' '.join(systlists[syst])
                # datacard preparation
                cmd = 'python %s --date %s --model %s --regslist %s --regsname %s --fresh False --systlist %s --systname %s --year %s' % (dcscr, date, m, srlisttxt, sr, systtxt, syst, year)
                print cmd
                os.system(cmd)

