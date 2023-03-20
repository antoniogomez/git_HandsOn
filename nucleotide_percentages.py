#!/usr/bin/env python

# Script to calculate the proportion of nucleotides in a DNA or RNA sequence

# Import packages and functions required
import sys, re
from argparse import ArgumentParser

# Specifies the input arguments that will be received
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

# Exit the script if the input sequence's length is 1
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Specifies the input arguments that will be received
parser = ArgumentParser(description = 'Calculate the proportion of nucleotides in a DNA or RNA sequence')
parser.add_argument('-s', "--seq", type = str, required = True, help = 'Input sequence')

# Calculate the proportion of nucleotide in a DNA or RNA sequence

args = parser.parse_args()
args.seq = args.seq.upper() # Transforms the sequence in upper case

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
