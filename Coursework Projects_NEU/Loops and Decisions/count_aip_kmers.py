#!/usr/bin/env python
#aip_kmers
import re
import os
read_sample = open('/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq','r')
aline = ' '
kmer_length = 6
kmer_dictionary = {}
while aline:
    aline = read_sample.readline()
    aline = aline.rstrip(os.linesep)
    if re.match('^[ATGCN]+$', aline):
        stop = len(aline) - kmer_length + 1
        for start in range(0,stop):
            kmer = aline[start:start +  kmer_length]
            if kmer in kmer_dictionary:
                kmer_dictionary[kmer] += 1
            else:
                kmer_dictionary[kmer] = 1
t = '\t'
aip_kmers = open("aip_kmers.txt",'w')
for kmer in kmer_dictionary:
    count = kmer_dictionary[kmer]
    out = (kmer, str(count))
    aip_kmers.write(t.join(out) + "\n")
