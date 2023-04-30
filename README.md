# razorlimits

Limit setting code for the CMS razor boost analysis

Scripts and other relevant files:

-- makedatacards_rzr.py : Prepares datacards from razor boost analysis output files.  Can select model and signal region / set of signal regions.

-- rundatacards.py : Runs makedatacards_rzr.py locally over a defined set of models for different SRs / SR sets.
Use this script for locally testing / validating datacard creation.

-- temps/runlimits_rzr_temp.py : Template script running limits for a given model and SR / SR set.
For a given model, the job runs over all points.

-- rundclimits_temp.sh : Template script for running the makedatacards_rzr.py and temps/runlimits_rzr_temp.py sequence for a given model and SR / SR set.

-- submitdclimitjobs.py : Creates datacards, then runs limits for a given list of models and SRs / SR sets.
The script prepares jobs for each SR / SR set in each model.  It creates scripts from temps/runlimits_rzr_temp.py and rundclimits_temp.sh .
For a given model, the job runs over all points.
This is the main script to use for mass-producing limits.
If condor jobs stop before all limits are calculated, one can resubmit by rerunning this script.

-- Get2DContour.py : Produces 2D maps and contours for each model and each SR / SR set from all points with calculated limits.

-- runcontours.py : The script that automates running Get2DContour.py over multiple models and SRs / SR sets.

-- SMSPlottingCode/runplots.py : Produces final limit plots from created 2D maps and contours for a list of given models and SRs / SR sets.

-- SMSPlottingCode/configs/ : Directory that contains template config files for plot-making by SMSPlottingCode/runplots.py and the scripts within.


Steps:

In all steps below, the models and SRs / SR lists can be defined / modified within the scripts.

0. Modify paths to your local installation in 
makedatacards_rzr.py , /submitdclimitjobs.py , temps/runlimits_rzr_temp.py , temps/rundclimits_temp.sh
(search for "modify path")

1. If necessary, test datacard creation (e.g. when there is a new set of signal/BG files, new binning, new systematic...)
python rundatacards.py <date>
(entering a date allows to distinguish between different limits for the same signal / SR)
Datacards are created under the "datacards/<date>" directory for each model and SR / SR set in subdirectories named accordingly.

2. If datacard tests are successful, run the datacard + limit jobs:
python submitdclimitjobs.py <date>
First, datacards should occur under directory "datacards/<date>".
Then limit results should occur under directories:
-- logfiles/<date> : Combine text outputs
-- limitsroot/<date> : Combine root outputs
-- limits2root/<date> : Combine outputs converted to input for contour calculation.

3. Create 2D maps and contours:
python runcontours.py <date>
Results will be produced under limits2root/<date>/<model>_<SRsname>/results/

4. Create plots:
cd SMSPlottingCode
python runplots.py <date>
Plots will be produced in directory <date> under SMSPlottingCode.

