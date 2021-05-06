#Introduction: 
Short Read Alignment includes a set of procedures including trimming, aligning, sorting and indexing of RNA sequences extracted from a database which leads to the assembly of a transcriptome.


GSNAP is a major tool used as an aligner. Its steps include:
1) Quality trimming of reads
2) Building of an index of reference genome extracted from the GMAP database by using gmap_build
3) Building a database of known introns extracted from GFF3 file by using the iit_store command
4) Running the alignment using gsnap command
5) Sorting of sequences into BAM file#6) Indexing of sequences


##1) Quality Trimming of Reads
It is a well known fact that automated sequencers give rise to read that are of poor quality especially if they are quite long. Trimmomatic, a java based trimmer, is used for this assignment that determines if the quality scores have dropped below the threshhold using a sliding window. Furthermore, it gets rid of adapter sequences since they tend to complicate the procedure for assemblers and aligners. “trimALL” function was used to trim the sequences in this asignment.


##2) Building GMAP database
Using the shell script provided the GMAP database was built from Aiptasia genome. GMAP database is first indexed then optimized which results in a much faster alignment than it would be if fastq files were used instead.


##3) Extracting sequence from GFF3
GFF3 file contains the genes, introns and exons relative to the chromosomes in genome. It provides various infromation including the position of the abovementioned features using which the aligner guides alignment. 


##4) Aligning Sequences
The sequences extracted are read against or aligned to those in GMAP database. This is done to identify the regions of similarity which may occur either due to a structural, functional or even an evolutionary relationship between the sequences being studied. Sequences are aligned  using “alignALL” function and stored as “sam” files. SAM (Sequence Alignment Map) format is used for storing sequences geenrated by NGS technologies. It can store both short and long reads produced by different sequencing platforms and has been widely used in various major projects. 


#5) Sorting Sequences
Assemblers usually require sequences of SAM format to be sorted as that of BAM. BAM (Binary Alignment Map is the compressed binary version of SAM. “samtools” utilities are used for this purpose and can also be used for various other methods – Viewing, Sorting, Merging, Indexing. For example, BAM files being binary cannot be seen but by using the viewing tool of samtools they can be visualised. “sortALL” function is used to sort sequences.


##6) Indexing Sequences
“samtools” can be used to Index the above obtained sorted sequences. Index command enables a fast look-up of data in a sorted SAM/BAM format (BAM in this case). This command generates a *.bam.bai format file which can be read more efficiently to make the downstream processes smoother and more accurate. “indexALL” function is used here.


Through the abovementioned steps sequences are extracted, aligned with a genomic reference, trimmed, sorted and indexed. Through another set of processes the obtained data can be assembled into a transcriptome. 


##References:
*https://www.genecodes.com/sequencher-features/sequence-trimming

*Bolger, Anthony M., Marc Lohse, and Bjoern Usadel. "Trimmomatic: A Flexible Trimmer for Illumina Sequence Data." Bioinformatics 30.15 (2014): 2114-120. Web.
