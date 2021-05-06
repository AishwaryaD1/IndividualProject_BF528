#!/usr/bin/env python

#readFastq.py

from Bio import SeqIO

import itertools

leftReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")

firstFive = itertools.islice(leftReads, 5)

for left in firstFive:
    print(left.id)
