#!/usr/bin/env python

from Bio.Seq import Seq
dna = Seq("AGTACACTGGTA")
rna = dna.transcribe()
protein = rna.translate()
print(protein)
