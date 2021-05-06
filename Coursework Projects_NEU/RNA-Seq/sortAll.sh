#!/usr/bin/env bash
#sortAll.sh
#initialize variable to contain the directory of fastq file 
filepath="./sam/"
left=".sam"
newForm=".sorted.bam"
output="bam/"

#Create output directory
mkdir -p $output

#loop through all fastqfiles in $filepath
function sortAll {
for leftInFile in $filepath*$left
    do
        #Remove the path from the filename and assign to pathRemoved
        pathRemoved="${leftInFile/$filepath/}"
        
        #Removed left from $pathRemoved and assign to sampleName
        
        sampleName="${pathRemoved/$left}"
        samtools sort \
        $filepath$sampleName$left \
        -o $output$sampleName$newForm
    done
}
sortAll 1>sortAll.log 2>sortAll.err &
