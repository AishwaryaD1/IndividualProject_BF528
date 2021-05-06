#!/usr/bin/env bash
#indexAll.sh
#Initialize variable to extract .bam files from bam directory
filepath="./bam/"
left=".sorted.bam"

#loop through the bam files
function indexAll {
        for leftInFile in $filepath*$left
        do
        
        #remove path from filepath and assign to pathRemoved
        pathRemoved="${leftInFile/$filepath/}"
        
        #remove suffix from $pathRemoved and assign to sampleName
        sampleName="${pathRemoved/$left/}"
        samtools index $filepath$sampleName$left
        done
}
indexAll 1>indexAll.log 2>indexAll.err &
