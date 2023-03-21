#!/usr/bin/env python

# Script so that it is able to classify correctly any RNA or DNA sequence

# Packages and functions must be imported
import sys, re
from argparse import ArgumentParser

# Specifies the input arguments that will be received
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Exit the script if the input sequence's length is 1
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Determines if a sequence is made up of DNA or RNA.
# To prevent identifying a sequence including T and U as DNA or RNA, the phrase "if not" is included.
args = parser.parse_args()

args.seq = args.seq.upper()  # Note we just added this line
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        if not re.search('U', args.seq):
            print ('The sequence is DNA')
        else:
            print ('Please check the sequence, it contains both T and U')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')
    
# Analyze the sequence to find the motif (if provided)
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
