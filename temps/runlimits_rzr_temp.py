#/usr/bin/env python

import os,sys
from ROOT import *
from string import *

def getxsec(model):
    xsecdict = {} # dict for xsecs
    if 'T1' in model or 'T5' in model or 'R5' in model:
        # Modify path below to match your setup:
        xsecFile = "/afs/cern.ch/user/s/ssekmen/work/RazorRun2/limit/razorlimits/glu_xsecs_13TeV.txt"
    if 'T6' in model or 'T2tb' in model or 'R2' in model:
        # Modify path below to match your setup:
        xsecFile = "/afs/cern.ch/user/s/ssekmen/work/RazorRun2/limit/razorlimits/stopsbot_xsecs_13TeV.txt"
    if model == 'TChiWZ':
        xsecFile = "/afs/cern.ch/user/s/ssekmen/work/RazorRun2/limit/razorlimits/c1n2_xsecs_13TeV.txt"
    if model == 'TChiWW':
        xsecFile = "/afs/cern.ch/user/s/ssekmen/work/RazorRun2/limit/razorlimits/c1c1_xsecs_13TeV.txt"

    with open(xsecFile,"r") as xfile:
        lines = xfile.readlines()
        print 'Found %i lines in %s' %(len(lines),xsecFile)
        for line in lines:
            if line[0] == '#': continue
            (mparent,xsec,err) = line.split()
            xsecdict[int(mparent)] = (float(xsec),float(err))

    return xsecdict


def writeTree(box, model, directory, mg, mchi, xsecULObs, xsecULExpPlus2, xsecULExpPlus, xsecULExp, xsecULExpMinus, xsecULExpMinus2, signif):
    #tmpFileName = "%s/%s_xsecUL_mg_%s_mchi_%s_%s.root" %("/tmp", model, mg, mchi, box)
    outputFileName = "%s/%s_xsecUL_mg_%s_mchi_%s_%s.root" %(directory, model, mg, mchi, box)
    if ctau != '':
        outputFileName = "%s/%s_xsecUL_mg_%s_mchi_%s_ctau_%s_%s.root" %(directory, model, mg, mchi, ctau,  box)
    fileOut = TFile.Open(outputFileName, "recreate")

    if 1==1:
        xsecTree = TTree("xsecTree", "xsecTree")
        try:
            from ROOT import MyStruct
        except ImportError:
            myStructCmd = "struct MyStruct{Double_t mg;Double_t mchi; Double_t x; Double_t y;"
            ixsecUL = 0
            myStructCmd+= "Double_t xsecUL%i;"%(ixsecUL+0)
            myStructCmd+= "Double_t xsecUL%i;"%(ixsecUL+1)
            myStructCmd+= "Double_t xsecUL%i;"%(ixsecUL+2)
            myStructCmd+= "Double_t xsecUL%i;"%(ixsecUL+3)
            myStructCmd+= "Double_t xsecUL%i;"%(ixsecUL+4)
            myStructCmd+= "Double_t xsecUL%i;"%(ixsecUL+5)
            ixsecUL+=6
            myStructCmd += "}"
            gROOT.ProcessLine(myStructCmd)
            from ROOT import MyStruct
        
        s = MyStruct()
        xsecTree.Branch("mg", AddressOf(s,"mg"),'mg/D')
        xsecTree.Branch("mchi", AddressOf(s,"mchi"),'mchi/D')
        xsecTree.Branch("x", AddressOf(s,"x"),'x/D')
        xsecTree.Branch("y", AddressOf(s,"y"),'y/D')    
    
    s.mg = mg
    s.mchi = mchi
    if 'T1x' in model:
        s.x = float(model[model.find('x')+1:model.find('y')].replace('p','.'))
        s.y = float(model[model.find('y')+1:].replace('p','.'))
    elif model == 'T1bbbb':
        s.x = 1
        s.y = 0
    elif model == 'T1tttt':
        s.x = 0
        s.y = 1
    else:
        s.x = -1
        s.y = -1

    if 1==1:
        ixsecUL = 0
        xsecTree.Branch("xsecULObs_%s"%box, AddressOf(s,"xsecUL%i"%(ixsecUL+0)),'xsecUL%i/D'%(ixsecUL+0))
        xsecTree.Branch("xsecULExpPlus2_%s"%box, AddressOf(s,"xsecUL%i"%(ixsecUL+1)),'xsecUL%i/D'%(ixsecUL+1))
        xsecTree.Branch("xsecULExpPlus_%s"%box, AddressOf(s,"xsecUL%i"%(ixsecUL+2)),'xsecUL%i/D'%(ixsecUL+2))
        xsecTree.Branch("xsecULExp_%s"%box, AddressOf(s,"xsecUL%i"%(ixsecUL+3)),'xsecUL%i/D'%(ixsecUL+3))
        xsecTree.Branch("xsecULExpMinus_%s"%box, AddressOf(s,"xsecUL%i"%(ixsecUL+4)),'xsecUL%i/D'%(ixsecUL+4))
        xsecTree.Branch("xsecULExpMinus2_%s"%box, AddressOf(s,"xsecUL%i"%(ixsecUL+5)),'xsecUL%i/D'%(ixsecUL+5))
        exec 's.xsecUL%i = xsecULObs[ixsecUL]'%(ixsecUL+0)
        exec 's.xsecUL%i = xsecULExpPlus2[ixsecUL]'%(ixsecUL+1)
        exec 's.xsecUL%i = xsecULExpPlus[ixsecUL]'%(ixsecUL+2)
        exec 's.xsecUL%i = xsecULExp[ixsecUL]'%(ixsecUL+3)
        exec 's.xsecUL%i = xsecULExpMinus[ixsecUL]'%(ixsecUL+4)
        exec 's.xsecUL%i = xsecULExpMinus2[ixsecUL]'%(ixsecUL+5)
        ixsecUL += 4
        
        xsecTree.Fill()
        
        fileOut.cd()
        xsecTree.Write()
        
        fileOut.Close()
        
        #outputFileName = "%s/%s_xsecUL_mg_%s_mchi_%s_%s.root" %(directory, model, mg, mchi, box)
        print "INFO: xsec UL values being written to %s"%outputFileName
        
        #special_call(["mv",tmpFileName,outputFileName],0)
        
    return outputFileName

#--------------

# Gt the cross sections
box = 'Rzr'
#model = 'T1qqqqLL'
#model = 'T2btLL'
model = 'modelname'
#model = 'T6ttZH'
#model = 'PureHiggsino'
dirext = 'dirextname'
#dirext = '_SR_Had_1htop'
date = 'datename'
#ctauchoice = 'ctauctauname'
ctauchoice = ''

# Modify path below to match your setup:
maindir = '/afs/cern.ch/user/s/ssekmen/work/RazorRun2/limit/razorlimits/'
dcdir = maindir+'datacards/'+date+'/'+model+dirext+'/'
limitdir = maindir+'limitsroot/'+date+'/'+model+dirext+'/'
limit2dir = maindir+'limits2root/'+date+'/'+model+dirext+'/'
logdir = maindir+'logfiles/'+date+'/'+model+dirext+'/'
if not os.path.exists(limitdir):
    os.system('mkdir -p '+limitdir)
if not os.path.exists(limit2dir):
    os.system('mkdir -p '+limit2dir)
if not os.path.exists(logdir):
    os.system('mkdir -p '+logdir)

dcs = os.popen('ls '+dcdir+'*.txt').readlines()

# read the cross sections:
xsecdict = getxsec(model)

# write results to a tree

for dc in dcs:
    dc = strip(dc)
    if "_Glu" in dc: continue
    if not ctauchoice in dc: continue
    fln = replace(split(split(dc, '/')[-1], '.')[0], "datacard", "") 

    xsecULObs	= 0.
    xsecULExpMinus2 = 0.
    xsecULExpMinus  = 0.
    xsecULExp	= 0.
    xsecULExpPlus   = 0.
    xsecULExpPlus2  = 0.
    signif          = 0.

    logfile = logdir+fln+'.log'
    #if os.path.exists(logfile):
    #    continue
    limitfln = limitdir+'higgsCombine'+fln+'.AsymptoticLimits.mH120.root'
    print 'Running:', limitfln
    if os.path.exists(limitfln): continue
#    cmd = 'combine -M AsymptoticLimits '+dc+' --name '+fln+' >& '+logfile
    cmd = 'combine -M AsymptoticLimits '+dc+' --name '+fln+' --run blind >& '+logfile
    print cmd
    os.system(cmd)
    os.system('mv *'+fln+'*.root '+limitfln)
    mparent = int(fln.split('_')[1])
    print mparent, fln
    mLSP = int(fln.split('_')[2])
    ctau = ''
    if 'T1qqqq' in model:
        mparent = int(limitfln[limitfln.find('Glu')+3:limitfln.find('_Chi')])
        mLSP = int(limitfln[limitfln.find('Chi1ne')+6:limitfln.find('.As')])   
    if 'T2bt' in model:
        mparent = int(limitfln[limitfln.find('Stop')+4:limitfln.find('_Chi')])
        #mLSP = int(limitfln[limitfln.find('Chi1ne')+6:limitfln.find('.As')])   
        mLSP = int(limitfln[limitfln.find('Chi1ne')+6:limitfln.find('_ctau')])   
        ctau = int(limitfln[limitfln.find('_ctau')+5:limitfln.find('.As')])   
    if 'T1btbt' in model:
        mparent = int(limitfln[limitfln.find('Glu')+3:limitfln.find('_Chi')])
        mLSP = int(limitfln[limitfln.find('Chi1ne')+6:limitfln.find('_ctau')])   
        ctau = int(limitfln[limitfln.find('_ctau')+5:limitfln.find('.As')])   
    if 'T2tb' in model:
        mparent = int(limitfln[limitfln.find('Sbottom')+7:limitfln.find('_Chi')])
        mLSP = int(limitfln[limitfln.find('Chi1ne')+6:limitfln.find('_ctau')])   
        ctau = int(limitfln[limitfln.find('_ctau')+5:limitfln.find('.As')])   
    if 'PureHiggsino' in model:
        mparent = int(limitfln[limitfln.find('Sbottom')+7:limitfln.find('_Chi')])
        mLSP = int(limitfln[limitfln.find('Chi1ne')+6:limitfln.find('_ctau')])
    print 'mparent, mchi', mparent, mLSP, ctau
    log = open(logfile).readlines()
    mparent = int(5*round(mparent/5))
    refXsec = xsecdict[mparent][0]
    print mparent, refXsec
    for line in log:
        if "Observed Limit:" in line:
            xsecULObs = refXsec*float(line.split()[4])
        elif "Expected  2.5%:" in line:
            xsecULExpMinus2 = refXsec*float(line.split()[4])
        elif "Expected 16.0%:" in line:
            xsecULExpMinus = refXsec*float(line.split()[4])
        elif "Expected 50.0%:" in line:
            xsecULExp = refXsec*float(line.split()[4])
        elif "Expected 84.0%:" in line:
            xsecULExpPlus = refXsec*float(line.split()[4])
        elif "Expected 97.5%:" in line:
            xsecULExpPlus2 = refXsec*float(line.split()[4])
        elif "Significance:" in line:
            signif = float(line.split()[1])

    print "Exp limit:", xsecULExp
    writeTree(box, model, limit2dir, float(mparent), float(mLSP), [xsecULObs], [xsecULExpPlus2], [xsecULExpPlus], [xsecULExp], [xsecULExpMinus], [xsecULExpMinus2], 0)


