#!/usr/bin/env bash
blastx -query /scratch/SampleDataFiles/Seq.fasta \
-db /blastDB/swissprot \
-num_alignments 5 \
-outfmt "6 qseqid sacc qlen slen length nident pident evalue stitle"
