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
  "--systlist",   # name on the CLI - drop the `--` for positional/required parameters
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
  "--year",  # name on the CLI - drop the `--` for positional/required parameters
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
  "--systname",  # name on the CLI - drop the `--` for positional/required parameters
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
systname = args.systname
year = args.year

gStyle.SetOptStat(0)
gStyle.SetPalette(1)

gStyle.SetTextFont(42)

gStyle.SetTitleStyle(0000)
gStyle.SetTitleBorderSize(0)
#gStyle.SetTitleFont(42)
#gStyle.SetTitleFontSize(0.055)

#gStyle.SetTitleFont(42, "xyz")
#gStyle.SetTitleSize(0.5, "xyz")
#gStyle.SetLabelFont(42, "xyz")
#gStyle.SetLabelSize(0.45, "xyz")

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

systpick = [
    "",
    "_jesUp",
    "_jesDown",
    "_jerUp",
    "_jerDown",
    "_BoostTagUp",
    "_BoostTagDown",
    "_BoostTag_FastsimUp",
    "_BoostTag_FastsimDown",
    "_BoostmisTagUp",
    "_BoostmisTagDown",
]

systpick = args.systlist
systpick.insert(0, "")
print "systpick" , systpick

systdict = {
    "" : 1,
    "_topptUp" : 2,
    "_topptDown" : 3,
    "_isrUp" : 4,
    "_isrDown" : 5,
    "_pileupUp" : 6,
    "_pileupDown" : 7,
    "_L1PreFiringUp" : 8,
    "_L1PreFiringDown" : 9,
    "_alphasUp" : 10,
    "_alphasDown" : 11,
    "_scaleUp" : 12,
    "_scaleDown" : 13,
    "_lostlepUp" : 14,
    "_lostlepDown" : 15,
    "_triggerUp" : 16,
    "_triggerDown" : 17,
    "_jesUp" : 18,
    "_jesDown" : 19,
    "_jerUp" : 20,
    "_jerDown" : 21,
    #"_metUp",
    #"_metDown",
    #"_RescaleAK8Up",
    #"_RescaleAK8Down",
    "_puidUp" : 22,
    "_puidDown" : 23,
    "_BoostTagUp" : 24,
    "_BoostTagDown" : 25,
    "_BoostTag_FastsimUp" : 26,
    "_BoostTag_FastsimDown" : 27,
    "_BoostmisTagUp" : 28,
    "_BoostmisTagDown" : 29,
    #"_BoostmisTag_FastsimUp",
    #"_BoostmisTag_FastsimDown",
    #"_EleRecoUp",
    #"_EleRecoDown",
    #"_EleIDUp",
    #"_EleIDDown",
    #"_EleIsoUp",
    #"_EleIsoDown",
    "_EleFullsimUp" : 30,
    "_EleFullsimDown" : 31,
    "_EleFastsimUp" : 32,
    "_EleFastsimDown" : 33,
    #"_PhoIDUp",
    #"_PhoIDDown",
    #"_MuonTrackUp",
    #"_MuonTrackDown",
    "_MuonFullsimUp" : 34,
    "_MuonFullsimDown" : 35,
    "_MuonFastsimUp" : 36,
    "_MuonFastsimDown" : 37,
    "_BTagUp" : 38,
    "_BTagDown" : 39,
    "_BTagFastsimUp" : 40,
    "_BTagFastsimDown" : 41,
    "_cf_QTWUp" : 42,
    "_cf_QTWDown" : 43,
    "_cf_ZUp" : 44,
    "_cf_ZDown" : 45,
    "_cf_NonIso_Up" : 46,
    "_cf_NonIso_Down" : 47,
}

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
    fb = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/'+year+'_'+p+'.root')
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
fdata = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/'+year+'_Data.root')
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
fs = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/'+year+'_SMS-'+modelfn+'_TuneCP5_13TeV-madgraphMLM-pythia8.root')
#fs = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/SMS-TChiWWpm-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8.root')
#fs = TFile('/eos/cms/store/user/chuh/RazorBoost/limit/SMS-TChiWZ-mNLSP200To1500_mLSP0To600_TuneCP5_13TeV-madgraphMLM-pythia8.root')
fs.cd('Signal')
for k in gDirectory.GetListOfKeys():
    kn = k.GetName()
    if not SRs[0] in kn: continue
    spt = kn.split('__')[1]
    if spt not in sigpts: sigpts.append(spt)


c = TCanvas("c", "c", 1700, 500)
c.SetGrid()

# Number of background processes
nbg = str(len(procs) - 1)
nch = 0

#print hbgs

# Assuming you have a list of TH2D histogram objects named hbgs[0]
# and you want to sum the GetXaxis().GetNbins() attribute for each of them.

# Create a lambda function to extract the values you want from each histogra
sum_lambda = lambda th2d: th2d.GetXaxis().GetNbins()

# Use the sum function to sum the values in the list
nxbins = sum(map(sum_lambda, hbgs[0]))

print nxbins

cols = [kBlack, kAzure+7, kGreen+1, kViolet-4, kCyan+1, kOrange+1, kBlue-3]

for hsrs in hbgs:
    print hsrs
    print '\n'
    #for h in hsrs:
    #    nbins = h.GetXaxis().GetNbins(), h.GetYaxis().GetNbins()
    #    print h.GetName(), h.GetXaxis().GetNbins(), h.GetYaxis().GetNbins()
    syshistos = []
    for s in systpick:
        h1d = TH1D(hsrs[0].GetName()+s, hsrs[0].GetName()+s, nxbins, 1, nxbins)
        ib = 1
        for h in hsrs:
            for ixb in range(1, h.GetXaxis().GetNbins()+1):
                if h.GetBinContent(ixb, 1) != 0:
                    h1d.SetBinContent(ib, h.GetBinContent(ixb, systdict[s]) / h.GetBinContent(ixb, 1))
                ib = ib + 1
        print h1d.GetName(), h1d.Integral()
        syshistos.append(h1d)

    l = TLegend(0.12, 0.71, 0.72, 0.88)
    l.SetNColumns(4)
    l.SetBorderSize(0)
    l.SetFillStyle(0000)
    l.SetTextSize(0.040)
    l.SetTextFont(42)
    for i in range(len(syshistos)):
#    for i in range(1):
        print i
        hs = syshistos[i]
#        hs.Divide(hsdenom)
        print hs.GetName(), hs.Integral()
        hs.SetMaximum(3)
        hs.SetMinimum(0)
        if i % 2 == 0: 
            hs.SetLineWidth(3)
            hs.SetLineStyle(2)
        else:
            hs.SetLineWidth(1)
        hs.SetLineColor(cols[(i / 2) + i % 2])
        if i == 0 : hs.SetLineColor(kWhite)
#        if i > 0 : hs.SetLineStyle((i % 2) + 1)
        if i == 0:
            process = hs.GetName().split("_")[2]
            hs.SetTitle("")
            hs.Draw()
        else:
            hs.Draw("same")
        if i > 0: l.AddEntry(hs, systpick[i], "l")

    t = TLatex(0.76, 0.82, process+', all SRs, '+year)
    t.SetNDC()
    t.Draw("same")

    l.Draw("same")
    c.Print('SRs_'+regsname+'_'+process+'_'+systname+'_'+year+'.png')

