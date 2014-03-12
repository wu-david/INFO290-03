#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from ftp://ftp.fec.gov/FEC/2012/pas212.zip - data dictionary is at
http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionstoCandidates.shtml
"""

import fileinput
import csv


donations = [float(row[14]) for row in csv.reader(fileinput.input(), delimiter='|')]
candidates = set([row[16] for row in csv.reader(fileinput.input(), delimiter='|')])
total = sum(donations)
minimum = min(donations)
maximum = max(donations)
mean = total / float(len(donations))
donations.sort()
median = donations[len(donations)/2]
std = 0.0
for num in donations:
    std += (num - mean) ** 2
std = std/float(len(donations))
std = std**0.5

        ###
        # TODO: calculate other statistics here
        # You may need to store numbers in an array to access them together
        ##/

###
# TODO: aggregate any stored numbers here
#
##/

##### Print out the stats
print "Total: %s" % total
print "Minimum: %s" % minimum
print "Maximum: %s" % maximum
print "Mean: %s" % mean
print "Median: %s" % median
# square root can be calculated with N**0.5
print "Standard Deviation: %s" % std

##### Comma separated list of unique candidate ID numbers
print "Candidates: %s" % candidates

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    norm = float(value - minimum) / float(maximum - minimum) * (1 - 0) + 0
    ###/

    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])
