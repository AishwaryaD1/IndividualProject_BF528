#!/usr/bin/env python

from Bio import SeqIO
import itertools

leftReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")

firstFive = itertools.islice(leftReads, 5)
SeqIO.write(firstFive, "slice.fastq", "fastq")


