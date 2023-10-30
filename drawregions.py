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
    "_cf_ZUp",
    "_cf_ZDown",
    "_cf_NonIso_Up",
    "_cf_NonIso_Down",
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

c = TCanvas("c", "c", 1700, 500)


# Number of background processes
nbg = str(len(procs) - 1)
nch = 0


def drawsgbg(hd, hb, hs, sig, c):
    c.SetLogy(1)
    hmax = hd.GetMaximum()
    print(hd.GetMaximum())
    for h in hb:
#        if h.GetMaximum() > hmax: hmax = h.GetMaximum()
        print(h.GetMaximum())

    l = TLegend(0.58, 0.57, 0.90, 0.87)
    l.SetBorderSize(0)
    l.SetFillStyle(0000)
    l.SetTextSize(0.040)
    l.SetTextFont(42)
    l.AddEntry(hd,'%-10s %-6s' % ('Data', str(round(hd.Integral(), 1))), 'p')
    
    c.cd()

    hbgstack = THStack("hbgstack", "")

    cols = [kAzure+7, kGreen+1, kViolet-4, kCyan+1, kOrange+1]
    i = 0 
    for	h in hb:
        h.SetLineColor(cols[i])
        h.SetFillColor(cols[i])
        h.SetLineWidth(0)
        hbgstack.Add(h)
        l.AddEntry(h, '%-10s %-6s' % (h.GetName().split('_')[2], str(round(h.Integral(), 1))), 'f')
        i = i + 1

    hbgstack.SetMaximum(hmax*1.2)
    hbgstack.Draw("h")

    hs.SetLineColor(kRed+1)
    hs.SetLineStyle(1)
    hs.SetLineWidth(3)
    hs.Draw("hist same")
    l.AddEntry(hs, '%-10s %-6s' % (sig, str(round(hs.Integral(), 1))), 'l')
    hd.SetLineColor(kBlack)
    hd.GetXaxis().SetLimits(0,1000)
    hd.SetMarkerStyle(20)
    hd.SetMarkerSize(1)
    #hd.Draw("p same")

    #l.AddEntry(hs,'#tilde{g}#tilde{g} signal', 'f')
    l.Draw("same")
    # Make the legend visible (annoying pyROOT-specific feature)
    SetOwnership(l, 0 )

    c.Print(hd.GetName()+'.png')

sig = '1000_100'
# Number of data events
for s in range(len(SRs)):
    hbgods = []
    for b in range(len(hbgs)):
        print hbgs[b][s].GetName()
        h = hbgs[b][s].ProjectionX(hbgs[b][s].GetName(), 1, 1)
        hbgods.append(h)
    #hstd = fs.Get("Signal/MRR2_S_signal_"+SRs[s].strip()+"__"+sig)
    hsname = "Signal/MRR2_S_signal_"+SRs[s].strip()+"_new__"+sig
    print hsname
    hstd = fs.Get("Signal/MRR2_S_signal_"+SRs[s].strip()+"_new__"+sig)
    hs = hstd.ProjectionX(hstd.GetName()+'_proj', 1, 1)
    drawsgbg(hdt[s], hbgods, hs, sig, c)


sys.exit()



