# Check the status of limits jobs.
# Outputs for each process and region 
# how many points there are, how many are done and what is the done percentage.
# Also outputs how many processes are complete and how many are incomplete.

#!/usr/bin/env python

import os,sys
from string import *

if len(sys.argv) < 2: 
    print '\n *** Run as: pyton '+sys.argv[0]+' <date>\n'
    sys.exit(0)

date = sys.argv[1]
print "\nDate: "+date

procs = os.popen('ls datacards/'+date).readlines()

procs = list(map(lambda x: x.strip(), procs))
#print procs

res = {}

procdone = 0
procnotdone = 0
print "%-18s %6s %6s %8s\n" % ("Process", "Points", "Done", "% done")
for p in procs:
    np = os.popen('ls datacards/'+date+'/'+p+' | wc -l').read()
    npdone = os.popen('ls limits2root/'+date+'/'+p+' | wc -l').read()
    np = float(np)
    npdone = float(npdone) 
    if np > 0: 
        percdone = 100 * npdone / np
    else: percdone = 0
    if percdone < 100:
        print "%-18s %6d %6d %8.2f" % (p, np, npdone, percdone)
        procnotdone = procnotdone + 1
    else: 
        procdone = procdone + 1

print "\n"
print "%-35s: %3d" % ("Number of completed processes ", procdone)
print "%-35s: %3d" % ("Number of not completed processes ", procnotdone)
