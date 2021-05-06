#!/usr/bin/env python

from Bio.Seq import Seq
dna = Seq("AGTACACTGGTA")
rna = dna.transcribe()
print(rna)
