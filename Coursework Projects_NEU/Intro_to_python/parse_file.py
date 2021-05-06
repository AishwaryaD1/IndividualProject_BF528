#!/usr/bin/env python
#parse_file.py

import re
dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'
line_count = 0;
seq = ''
with open(dmel_genome_path) as dmel_genome:
    for line in dmel_genome:
        line_count+= 1
        if line_count < 5:
            if re.match('^>', line):
                print(line)
            else:
                seq += line
print(seq) 
