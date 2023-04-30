#!/bin/sh

export SCRAM_ARCH=slc6_amd64_gcc530
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
export VO_CMS_SW_DIR=/cmsset_default.csh
source /cvmfs/cms.cern.ch/cmsset_default.sh

# Modify path below to match your setup:
cd /afs/cern.ch/user/s/ssekmen/work/RazorRun2/limit/CMSSW_12_2_3/src/
eval `scramv1 ru -sh`
cd dirname
dccommand

# Modify path below to match your setup:
cd /afs/cern.ch/user/s/ssekmen/work/RazorRun2/limit/CMSSW_10_2_13/src/
eval `scramv1 ru -sh`
cd dirname
python scriptname
