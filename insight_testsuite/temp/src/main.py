import numpy as np
import pandas as pd
import csv
import os
from utils import *
from collections import defaultdict
import math
from optparse import *
import sys



'''
Process following fields only
CMTE_ID: identifies the flier, which for our purposes is the recipient of this contribution
NAME: name of the donor
ZIP_CODE: zip code of the contributor (we only want the first five digits/characters)
TRANSACTION_DT: date of the transaction
TRANSACTION_AMT: amount of the transaction
OTHER_ID: a field that denotes whether contribution came from a person or an entity
'''

def validate_contr_rec(row):
    retVal = False
    if (row['TRANSACTION_DT'] == ''):
        retVal = False
    if(len(row['OTHER_ID']) == 0):
        if (len(row['ZIP_CODE']) == 5  or len(row['ZIP_CODE']) == 9) and row['ZIP_CODE'].isnumeric() == True and int(row['ZIP_CODE']) > 0:
            if (len(row['CMTE_ID']) > 1):
                if (len(row['TRANSACTION_AMT']) > 1) and (row['TRANSACTION_AMT'].isnumeric() == True) and int(row['TRANSACTION_AMT']) > 0:
                    if (len(row['NAME']) > 1):
                        if (len(row['TRANSACTION_DT'].rstrip()) == 8) and (row['TRANSACTION_DT'].isnumeric() == True) and (row['TRANSACTION_DT']):
                            year = int(row['TRANSACTION_DT'][4:8])
                            if year >= EARLIEST_YEAR and year <= datetime.now().year:
                                retVal = True
                            else:
                                retVal = False
                        else:
                            retVal = False
                    else:
                        retVal = False
                else:
                    retVal = False
            else:
                retVal = False
        else:
            retVal = False
    else:
        retVal = False
    return(retVal)

def read_itcont_file(fname):
    donors_data = defaultdict(list)
    cmte_data = defaultdict(list)
    if not os.path.exists(fname):
        print("Unable to locate PATH: " + fname )
    else:
        try:
            with open( fname,  "r",errors='ignore',) as contf: ## ignore encoding error during reading the file
                print(fname + " Opened successfully...")
                reader = csv.DictReader(contf,fieldnames = ITCONT_FIELD_NAMES, delimiter='|')
                dot = 0
                global min_year
                global max_year
                min_year = 0
                max_year = 0
                for row in reader:
                        ## Find record of valid individual contributor
                        if (validate_contr_rec(row) == True):
                            dot = dot + 1
                            zip_c = row['ZIP_CODE'][0:5]
                            cmte_id = row['CMTE_ID']
                            donated_amount = int(row['TRANSACTION_AMT'])
                            if (len(row['TRANSACTION_DT'])) == 0:
                                pass
                            else:
                                year = int(row['TRANSACTION_DT'][4:8])
                                if year < EARLIEST_YEAR or year > datetime.now().year: ## should never hit this condition
                                    print(row['TRANSACTION_DT'])
                                if year > max_year:
                                    max_year = year
                                if min_year == 0:
                                    min_year = year
                                if year < min_year:
                                    min_year = year
                                donor_name = row['NAME']
                                key = zip_c + ":" + donor_name
                                donation = (year, donated_amount,cmte_id)
                                donors_data[key].append(donation)
                                cmte_data[key].append(cmte_id)
                            if (dot % 500) == 0:
                                print(str(dot) + " Valid Records processed ", end="\r")
            print("File processing complete. " + "Min Year = " + str(min_year) + ", Max Year = " + str(max_year))
            return(donors_data)

        except IOError:
            print("Could not find the Input file : " + fname)


def read_prcntl_file(fname):
    percentile = -1
    if not os.path.exists(fname):
        print("Unable to locate PATH: " + f )
    else:
        try:
            with open(fname,"r") as contf:
                print(fname + " Opened successfully...")
                reader = csv.reader(contf, delimiter=' ')
                for row in reader:
                    if len(row) !=1:
                        print("Invalid format: " + fname)
                    else:
                        try:
                            percentile = int(row[0])
                            if (percentile < 0) or (percentile > 100):
                                percentile = -1
                        except ValueError:
                            print("Invalid Percentile Value: " + fname)

        except IOError:
            print("Could not find the Input file : " + fname)
    return(percentile)

def create_output_data_file(donor_data, prctl,fname):
    print("Analyzing filtered Donor data of size = ",len(donor_data)," Items")
    output_arr = np.empty(0)
    dot = 0
    for key in donor_data:
        split_key = key.split(":")
        zip_c = split_key[0]
        name = split_key[1]
        donation_to_cmte = defaultdict(list)
        prev_year_donor = False
        curr_year_donor = False
        repeat_donor = False
        donate_inst = defaultdict(int)
        for i in range(0,len(donor_data[key])):
            cyear = int(donor_data[key][i][0])
            donated = int(donor_data[key][i][1])
            cmte = donor_data[key][i][2]
            if cyear < max_year:
                prev_year_donor = True
            if cyear == max_year:
                curr_year_donor = True
            donation_to_cmte[cyear].append((donated,cmte))
        if (curr_year_donor == True) and (prev_year_donor == True):
            i = 0
            idx = 0
            for d in donation_to_cmte:
                if d == max_year:
                    #print(name + " resident of " + str(zip_c) + " is a repeat donor. Donated  $" + str(donation_to_cmte[d][i][0]) + " for " + str(donation_to_cmte[d][i][1]))
                    #print(str(donation_to_cmte[d][i][1]) + "|" + str(zip_c) + "|" + str(d) + "|" + " " + "|" + str(donation_to_cmte[d][i][0]) + "|" + " ")
                    for x in (donation_to_cmte[d][i][1], zip_c, int(d) , " " , int(donation_to_cmte[d][i][0]), " "):
                        output_arr = np.append(output_arr,x)
                    output_arr = np.reshape(output_arr,(-1,6))
        if (dot % 1) == 0:
            print(str(dot) + " Items Processed", end="\r")
        dot = dot + 1

    if len(output_arr) > 0:
        output_arr = output_arr[output_arr[:,0].argsort()]
        u, indices = np.unique(output_arr[:,0], return_index=True)
        indices = np.append(indices, len(output_arr))
        end_flag = False
        for x in range(0, len(indices)):
            if end_flag == True:
                break
            s = indices[x]
            e = indices[x+1]
            if e == len(output_arr):
                end_flag = True
            idx = 1
            for k in range(s,e):
                output_arr[k,5] = str(idx) #add iterator in the last column
                idx = idx+1
            percentile_donation = nearest_rank_percentile(sorted(output_arr[s:e,4]),prctl)
            for k in range(s,e):
                output_arr[k,3] = str('%d'%(percentile_donation)) #insert percentile value after 3rd column


    pd_output_df = pd.DataFrame(output_arr)
    pd_output_df.to_csv(fname, sep="|", header=False, index=False)
    print("Analysis of Donor data is complete...")
    print("Total " + str(len(output_arr)) + " results saved in " + fname)

def main():
    params = parse_input_params()
    (opt, args) = params.parse_args()
    percentile_val = read_prcntl_file(opt.fpercentile)
    if (percentile_val != -1):
        processed_data = read_itcont_file(opt.finput)
        create_output_data_file(processed_data,percentile_val,opt.foutput)
    else:
        ## if precentile is invalid, create empty donors report file
        empty_arr = np.empty(0)
        pd_output_df = pd.DataFrame(empty_arr)
        pd_output_df.to_csv(opt.foutput, sep="|", header=False, index=False)
        print("Analysis complete: Invalid Percentile Value")
        print("Results Saved in " + opt.foutput)

if __name__ == "__main__":
    main()
