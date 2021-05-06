#!/usr/bin/env bash
#align_spades.sh

function align_spades {
    nice -n19 python3.4 /usr/local/programs/SPAdes-3.10.0-Linux/bin/spades.py \
    -o $DIRECTORY \
    -1 PAIRED/SRR522244_1.paired.fastq \
    -2 PAIRED/SRR522244_2.paired.fastq \
    --threads 6
}

DIRECTORY=Rhodo

mkdir $DIRECTORY

align_spades 1>align_spades.log 2>align_spades.er
