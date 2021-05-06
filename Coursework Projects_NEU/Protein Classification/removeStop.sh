#!/usr/bin/env bash
#removeStop.sh

sed 's/*//' ../BLAST/Trinity.fasta.transdecoder.pep | head -n500 >proteins.fasta
