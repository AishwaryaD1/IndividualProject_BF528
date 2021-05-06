#!/usr/bin/env python
import re
from Bio.Seq import Seq
dna = Seq("GGTCCGGGATGCCTGAATGGTACACTGGTAAGTACACTGTAAGTAAAAAAAA")
rna = dna.transcribe()
orf = (re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group())

print(orf)
