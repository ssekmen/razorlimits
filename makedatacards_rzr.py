#!/usr/bin/env python

# Make datacards for a given set of SRs.
# Defined for the CMS razor boost Run 2 analysis.

import os,sys
from ROOT import *
from string import *
import argparse

regions = argparse.ArgumentParser()
regions.add_argument(
  "--regslist",   # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=str,
  default=[],  # default if nothing is provided
)
regions.add_argument(
  "--date",  # name on the CLI - drop the `--` for positional/required parameters
#  nargs=1,  # 0 or more values expected => creates a list
  type=str,
  default=[],  # default if nothing is provided
)
regions.add_argument(
  "--model",  # name on the CLI - drop the `--` for positional/required parameters
#  nargs=1,  # 0 or more values expected => creates a list
  type=str,
  default=[],  # default if nothing is provided
)
regions.add_argument(
  "--regsname",  # name on the CLI - drop the `--` for positional/required parameters
#  nargs=1,  # 0 or more values expected => creates a list
  type=str,
  default=[],  # default if nothing is provided
)
regions.add_argument(
  "--fresh",  # name on the CLI - drop the `--` for positional/required parameters
#  nargs=1,  # 0 or more values expected => creates a list
  type=bool,
  default=[False],  # default if nothing is provided
)
# parse the command line
args = regions.parse_args()

date = args.date
model = args.model
fresh = False
#SRs = sys.argv[3]
regsname = args.regsname

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

SRs = ['SR_Had_1htop',
      'SR_Had_2htop',
]

SRs = args.regslist

print(date, model, SRs)

procs = [
    'Signal',
    'MultiJet',
    'Top',
    'WJets',
    'ZJets',
    'Other'
    ]

systematics = [
    "",
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
    "_lostlepUp",
    "_lostlepDown",
    "_triggerUp",
    "_triggerDown",
    "_jesUp",
    "_jesDown",
    "_jerUp",
    "_jerDown",
    #"_metUp",
    #"_metDown",
    #"_RescaleAK8Up",
    #"_RescaleAK8Down",
    "_puidUp",
    "_puidDown",
    "_BoostTagUp",
    "_BoostTagDown",
    "_BoostTag_FastsimUp",
    "_BoostTag_FastsimDown",
    "_BoostmisTagUp",
    "_BoostmisTagDown",
    #"_BoostmisTag_FastsimUp",
    #"_BoostmisTag_FastsimDown",
    #"_EleRecoUp",
    #"_EleRecoDown",
    #"_EleIDUp",
    #"_EleIDDown",
    #"_EleIsoUp",
    #"_EleIsoDown",
    "_EleFullsimUp",
    "_EleFullsimDown",
    "_EleFastsimUp",
    "_EleFastsimDown",
    #"_PhoIDUp",
    #"_PhoIDDown",
    #"_MuonTrackUp",
    #"_MuonTrackDown",
    "_MuonFullsimUp",
    "_MuonFullsimDown",
    "_MuonFastsimUp",
    "_MuonFastsimDown",
    "_BTagUp",
    "_BTagDown",
    "_BTagFastsimUp",
    "_BTagFastsimDown",
    "_cf_QTWUp",
    "_cf_QTWDown",
    "_cf_NonIso_Up",
    "_cf_NonIso_Down",
    "_cf_ZUp",
    "_cf_ZDown",
]

# binname
if len(regsname) > 0:
    binname = '_'+regsname
    if regsname == 'all': binname = ''
else:
    binname = ''
    for sr in SRs:
        binname = binname + '_' + sr 

print(regsname, binname)

# Modify path below to match your setup:
maindir = '/afs/cern.ch/user/s/ssekmen/work/RazorRun2/limit/razorlimits/'
outdcdir = maindir+'datacards/'+date+'/'+model+binname+'/'

if not os.path.exists(outdcdir):
    os.system('mkdir -p '+outdcdir)


# Get all BG files
fbs = []
for p in procs:
    if p == "Signal": continue
    fb = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/run2_'+p+'.root')
    fbs.append(fb)

# Get all BG histograms in a list
hbgs = []
i = 0
for p in procs:
    if p == "Signal": continue
    print(p)
    hbgssr = []
    # Get BG histogram lists for each SR:
    for sr in SRs:
        #h = fbs[i].Get("Background/MRR2_S_bkg_"+sr)        
        h = fbs[i].Get("Background/MRR2_S_bkg_"+sr+"_new")
        h.SetName("MRR2_S_"+p+"_"+sr+"_new")
        hbgssr.append(h)
    hbgs.append(hbgssr)
    i = i + 1

# Get data histogram lists 
fdata = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/run2_Data.root')
hdt = []
for sr in SRs:
    #h = gDirectory.Get("Data/MRR2_S_data_"+sr)        
    h = gDirectory.Get("Data/MRR2_S_data_"+sr+"_new")        
    #h.SetName("MRR2_Data_"+sr+"_new")
    #h.SetName("MRR2_Data_"+sr)
    hdt.append(h)

# Get list of signal mass points
sigpts = []
modelfn = model
if model == 'TChiWW': modelfn = 'TChiWWpm-mNLSP200To1500_mLSP0To600'
if model == 'TChiWZ': modelfn = 'TChiWZ-mNLSP200To1500_mLSP0To600'
fs = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/run2_SMS-'+modelfn+'_TuneCP5_13TeV-madgraphMLM-pythia8.root')
#fs = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/SMS-TChiWWpm-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8.root')
#fs = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/SMS-TChiWZ-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8.root')
fs.cd('Signal')
for k in gDirectory.GetListOfKeys():
    kn = k.GetName()
    if not SRs[0] in kn: continue
    spt = kn.split('__')[1]
    if spt not in sigpts: sigpts.append(spt)


# DATACARD CONTENT

# Write the datacard beginning lines
cnt = '''imax %s number of channels
jmax %s number of backgrounds
kmax * number of nuisance parameters
------------------------------------------------------------
observation                    %s
------------------------------------------------------------
'''
# Number of background processes
nbg = str(len(procs) - 1)
nch = 0

# Number of data events
ndatac = []
for s in range(len(SRs)):
    nch = nch + hdt[s].GetXaxis().GetNbins()
    for ibin in range(1, hdt[s].GetXaxis().GetNbins()+1):
         ndatac.append('%-16s' % int(hdt[s].GetBinContent(ibin)) + ('%-16s' % '')*int(nbg))

# Make datacard files
for sig in sigpts:
    hsg = []
    for sr in SRs:
        #h = fs.Get("Signal/MRR2_S_signal_"+sr+"__"+sig)
        h = fs.Get("Signal/MRR2_S_signal_"+sr+"_new__"+sig)
        hsg.append(h)
    dcn = outdcdir+model+'_'+sig+'.txt'
    if fresh: 
        dc = open(dcn, 'w')
    else:
        if os.path.exists(dcn): 
            continue
        else:
            dc = open(dcn, 'w')
    # Write the datacard header
    #print nbg, ndata, frn
    dc.write(cnt % (nch, nbg, ''.join(ndatac)))#ndata))

    # Write processes and rates
    row = '%-30s ' % 'bin'
    itbin = 0
    for s in range(len(SRs)):
        for ibin in range(1, hdt[s].GetXaxis().GetNbins()+1):
            itbin = itbin + 1
            for i in procs:
#                row = row+'%-16s' % (sr+'_'+str(ibin))
                row = row+'%-16s' % ('SRb'+str(itbin))
    dc.write(row+'\n')
    row = '%-30s ' % 'process'
    for s in range(len(SRs)):
        for ibin in range(1, hdt[s].GetXaxis().GetNbins()+1):
            for i in procs:
                row = row+'%-16s' % i
    dc.write(row+'\n')
    row = '%-30s ' % 'process'
    for s in range(len(SRs)):
        for ibin in range(1, hdt[s].GetXaxis().GetNbins()+1):
            for i in range(len(procs)):
                row = row+'%-16i' % i
    dc.write(row+'\n')
    row = '%-30s ' % 'rate'
    for s in range(len(SRs)):
        for ibin in range(1, hdt[s].GetXaxis().GetNbins()+1):
            row = row +'%-16s' % str(round(hsg[s].GetBinContent(ibin, 1),3))
            for b in range(len(hbgs)):
                bgyield = hbgs[b][s].GetBinContent(ibin, 1)
                if bgyield == 0: bgyield = 0.001
#                row = row +'%-16s' % str(round(bgyield,3))
                # Fix negative BG yields.  This caused an issue in Had_1V_0b_34j but not others ...
                row = row +'%-16s' % str(round(fabs(bgyield),3))
#                row = row +'%-16s' % str(round(hbgs[b][s].GetBinContent(ibin, 1),3))
    dc.write(row+'\n')
    dc.write('-----------------------------------------\n')
    # Loop over systematics
    for sy in range(1,len(systematics),2):
        row = '%-24s ' % systematics[sy][:-2] +'%-6s ' % 'lnN'
        for s in range(len(SRs)):
            for ibin in range(1, hdt[s].GetXaxis().GetNbins()+1):
                thing = '-'
                if hsg[s].GetBinContent(ibin, 1) > 0:
                    up = round(hsg[s].GetBinContent(ibin, sy+1) / hsg[s].GetBinContent(ibin, 1), 3)
                    down = round(hsg[s].GetBinContent(ibin, sy+2) / hsg[s].GetBinContent(ibin, 1), 3)
                    if up == 0: up = 0.001
                    if down == 0: down = 0.001
                    if down > 10 and up < 10: down = up
                    if down < 10 and up > 10: up = down
                    if down > 10 and up > 10: 
                        up = 1.15
                        down = 0.85
                    if up != 1 or down != 1:    
                        thing = str(down)+'/'+str(up)
                row = row +'%-16s' % thing
                #row = row + ' ' + str(hsg[s].GetBinContent(ibin, sy+1))
                for b in range(len(hbgs)):
                    thing2 = '-'
                    if hbgs[b][s].GetBinContent(ibin, 1) > 0:
                        up = fabs(round(hbgs[b][s].GetBinContent(ibin, sy+1) / hbgs[b][s].GetBinContent(ibin, 1), 3))
                        down = fabs(round(hbgs[b][s].GetBinContent(ibin, sy+2) / hbgs[b][s].GetBinContent(ibin, 1), 3))
                        if up == 0: up = 0.001
                        if down == 0: down = 0.001
                        if down > 10 and up < 10: down = up
                        if down < 10 and up > 10: up = down
                        if down > 10 and up > 10: 
                            up = 1.15
                            down = 0.85
                        if up != 1 or down != 1:
                            thing2 = str(down)+'/'+str(up)
                    row = row +'%-16s' % thing2
        dc.write(row+'\n')

    print(dcn, 'is done')
#    break


sys.exit()



