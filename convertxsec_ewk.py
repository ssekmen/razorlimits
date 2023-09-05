#!/usr/bin/env python

# Convert the format of the EWK cross sections in the twiki to the limit code input format.

import os,sys
from string import *

fin = 'c1n2_xsecs_13TeV_raw.txt'
fout = open('c1n2_xsecs_13TeV.txt', 'w')

xsecs = open(fin).readlines()

for x in xsecs:
    x = split(strip(x))
    mass = x[0]
    xsec = atof(x[1]) / 1000.
    xsecerr = atof(x[2]) / atof(x[1]) * 100
    point = '%s %.4e %.2f \n' % (mass, xsec, xsecerr) 
    fout.write(point)
