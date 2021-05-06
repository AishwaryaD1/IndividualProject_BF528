#!/usr/bin/env bash

#alignReads.sh

#initialize variable to contain directory
filepath="./Paired/"
left=".R1.fastq"
right=".R2.fastq"
newForm=".sam"
output="sam/"

#create ouput directory
mkdir -p $output

#loop through all reads from pathfile
function alignReads {
    for leftInFile in $filepath*$left
    do
        #remove path from filename and assign to pathremoved
        pathRemoved="${leftInFile/$filepath/}"
        
        #remove left from $pathRemoved and assign to sampleName
        sampleName="${pathRemoved/$left/}"
        
        #print $sampleName to see what it contains after removing path
        echo $sampleName
        nice -n19 gsnap \
        -A sam \
        -D . \
        -d AiptasiaGmapDb \
        -s AiptasiaGmapIIT.iit \
        $filepath$sampleName$left \
        $filepath$sampleName$right \
        1>$output$sampleName$newForm
    done

}
alignReads 1>alignReads.log 2>alignReads.err &
