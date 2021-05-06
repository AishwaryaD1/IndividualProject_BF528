#!/usr/bin/env bash
#runQuast.sh

DIRECTORY="Quast/"
mkdir -p $DIRECTORY

function run_quast {
    nice -n19 /usr/bin/quast.py \
    -o $DIRECTORY \
    --threads 6 \
    -s \
    Rhodo/scaffolds.fasta
}
run_quast

#runquast 1>runquast.log 2>runquast.err
