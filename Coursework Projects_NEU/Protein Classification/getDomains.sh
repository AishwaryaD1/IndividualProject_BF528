#!/usr/bin/env bash
#getDmains.sh

cut -f13 proteins.tsv | sort | uniq > domains.txt
