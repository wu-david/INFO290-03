#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
from collections import *

(
    CMTE_ID, AMNDT_IND, RPT_TP, TRANSACTION_PGI, IMAGE_NUM, TRANSACTION_TP,
    ENTITY_TP, NAME, CITY, STATE, ZIP_CODE, EMPLOYER, OCCUPATION,
    TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID, CAND_ID, TRAN_ID, FILE_NUM,
    MEMO_CD, MEMO_TEXT, SUB_ID
) = range(22)

CANDIDATES = {
    'P80003338': 'Obama',
    'P80003353': 'Romney',
}

############### Set up variables
# TODO: declare datastructures
zip_dict = {}
candidate_dict = {candidate: 0 for candidate in CANDIDATES.itervalues()}
total = 0.0
############### Read through files
for row in csv.reader(fileinput.input(), delimiter='|'):
    candidate_id = row[CAND_ID]
    if candidate_id not in CANDIDATES:
        continue
    candidate_name = CANDIDATES[candidate_id]
    zip_code = row[ZIP_CODE]
    candidate_dict[candidate_name] += 1
    zip_dict.setdefault(zip_code, defaultdict(int))[candidate_name] += 1
    total += 1.0

def gini_index(values):
    total = float(sum(values))
    return 1 - sum([(float(value) / total) ** 2 for value in values])

def weight(value):
    return float(sum(value)) / total


gini = gini_index(candidate_dict.values()) # current Gini Index using candidate name as the class
split_gini = sum([weight(value.values()) * gini_index(value.values()) for value in zip_dict.itervalues()]) # weighted average of the Gini Indexes using candidate names, split up by zip code

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
