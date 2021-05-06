#!/usr/bin/env python
#interleave.py
#Import Seq, SeqRecord, SeqIO
from Bio import SeqIO

#import itertools to take slice of list
import itertools

leftReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
rightReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq", "fastq")

#Generate empty object
seq=[]

#Open interleaved fasta in write mode
outfile = open("interleaved.fasta","w")

#Iterate over both arrays in parallel
for left, right in zip(leftReads, rightReads):
    seq.append(left)
    seq.append(right)

SeqIO.write(seq, outfile, "fasta")
