#!/usr/bin/env python
# open_file.py

dmel_genome_path = '/scratch/Drosophile/dmel-all-chromosome-r6.17.fasta'

line_count =0;

with open(dmel_genome_path) as dmel_genome:
    for line in dmel_genome:
        line_count += 1
        if line_count < 5:
            print(line) 
