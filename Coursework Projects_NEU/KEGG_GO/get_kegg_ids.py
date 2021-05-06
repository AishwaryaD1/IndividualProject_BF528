#!/usr/bin/env python
#get_kegg_ids.py

import subprocess
#Open BLAST output
blast_output = open('../BLAST/alignPredicted.txt')
#Open files for stdout and stderr
out = open('kegg.txt','w')
err = open('kegg.err','w')
#Iterate over lines of the BLAST output
for blast_line in blast_output:
    #Remove the line terminator
    blast_line = blast_line.rstrip()
    #Split the line on whitespace
    fields = blast_line.split()
    sp = fields[1]
    evalue = fields[7]
    print(sp + "\t" + evalue)
    #Set evalue to less than 1e-180
    if float(fields[7]) < float("1e-180"):
        #Calling KEGG API
        result = subprocess.call("curl http://rest.kegg.jp/conv/genes/uniprot:" + sp,
        stdout=out, stderr=err, shell=True)
