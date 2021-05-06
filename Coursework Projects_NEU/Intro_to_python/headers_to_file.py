#!/usr/bin/env python
# headers_to_file.py
import re

drosophila_genome = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'
lct = 0;
seq=''

with open(drosophila_genome) as dm_genome:
    for line in dm_genome:
        if lct <50:
            if re.match('^>', line):
                seq+=line
                lct = lct + 1
      

with open("dmel_headers.txt", 'w') as out:
    out.write(seq) 

