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
        
# Script to calculate the proportion of nucleotides in a DNA or RNA sequence
nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'U': 0}

for nt in args.seq:
    if nt in nucleotide_counts:
        nucleotide_counts[nt] += 1

total_count = sum(nucleotide_counts.values())

if total_count == 0:
    print("Error: the input sequence contains no valid nucleotides.")
    sys.exit(1)

proportions = {nt: nucleotide_counts.get(nt, 0) / total_count * 100 for nt in nucleotide_counts.keys()}

print(f"The proportion of nucleotides in the sequence is as follows for A, C, G, T and U:\n"
      f"A: {proportions['A']:.2f}%\n"
      f"C: {proportions['C']:.2f}%\n"
      f"G: {proportions['G']:.2f}%\n"
      f"T: {proportions['T']:.2f}%\n"
      f"U: {proportions['U']:.2f}%\n")

