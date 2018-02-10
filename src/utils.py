
import math
from optparse import *
from datetime import datetime

'''
Author : Ashish Kumar
ashish@ashishkumar.org
02/10/2018
'''

ITCONT_FIELD_NAMES = ( 'CMTE_ID',
                        'AMNDT_IND',
                        'RPT_TP',
                        'TRANSACTION_PGI',
                        'IMAGE_NUM',
                        'TRANSACTION_TP',
                        'ENTITY_TP',
                        'NAME',
                        'CITY',
                        'STATE',
                        'ZIP_CODE',
                        'EMPLOYER',
                        'OCCUPATION',
                        'TRANSACTION_DT',
                        'TRANSACTION_AMT',
                        'OTHER_ID',
                        'TRAN_ID',
                        'FILE_NUM',
                        'MEMO_CD',
                        'MEMO_TEXT',
                        'SUB_ID')

ITCONT_INPUT_FILE='./input/itcont.txt'
PRCTL_INPUT_FILE='./input/percentile.txt'
OUTPUT_FILE = './output/repeat_donors.txt'
EARLIEST_YEAR = 1980


def nearest_rank_percentile(arr,prctl):
    # input array is in string
    # convert it into int, sort, calculate percentile index
    larr = []
    for n in arr:
       larr.append(int(n))
    larr = sorted(larr)
    arrSize = len(larr)
    n = (prctl/100*arrSize)
    return int(larr[math.ceil(n) - 1])

def parse_input_params():
    parser = OptionParser()
    parser.add_option("--input", type="string", dest="finput")
    parser.add_option("--percentile", type="string", dest="fpercentile")
    parser.add_option("--output", type="string", dest="foutput")
    parser.set_defaults(finput=ITCONT_INPUT_FILE, fpercentile=PRCTL_INPUT_FILE,
                        foutput=OUTPUT_FILE)
    return parser
