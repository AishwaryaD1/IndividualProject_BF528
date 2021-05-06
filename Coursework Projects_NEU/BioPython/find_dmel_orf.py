#!/usr/bin/env python

#find_dmel_orf.py
#Import Seq, SeqRecord and SeqIO 
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import re

#Reading Drosophila genome

for record in SeqIO.parse("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta", "fasta"):
    
    #Looking for full chromosomes not scaffolds
    if re.match("^\d{1}\D*$", record.id):
        dna = (record.seq)

        #Transcription of DNA

        rna = dna.transcribe()

        #Choosing the first AUG of orf

        orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
        
        #Change class from str to sequence     
        orf1=Seq(orf)
        
        #Translation of orf1 to protein

        protein = orf1.translate()

        print(protein)
