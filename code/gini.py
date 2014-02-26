#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv

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
obama = 0.0
romney = 0.0
zip_dict = {}
total = 0.0

############### Read through files
for row in csv.reader(fileinput.input(), delimiter='|'):
    candidate_id = row[CAND_ID]
    if candidate_id not in CANDIDATES:
        continue

    candidate_name = CANDIDATES[candidate_id]
    zip_code = row[ZIP_CODE]

    ###
    # TODO: save information to calculate Gini Index
    ##/
    if candidate_name == 'Obama':
        obama += 1.0
    else:
        romney += 1.0
    if zip_code in zip_dict:
        zip_dict[zip_code] += 1.0
    else:
        zip_dict[zip_code] = 1.0
    total += 1.0

###
# TODO: calculate the values below:
gini = 1.0 - ((obama/total)**2 + (romney/total)**2)  # current Gini Index using candidate name as the class
split_gini = 1.0 - sum([(frac/total)**2 for frac in zip_dict.values()])  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
