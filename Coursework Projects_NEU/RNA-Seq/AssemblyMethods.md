# Introduction:
Transcriptome Assembly or sequenced RNA assembly is a powerful skill to understand the molecular mechanisms to address biological questions. Transcriptome assembly is of two types: Reference-guided transcriptome  and de-novo transcriptome assembly. In reference-guided the positions of the reads are ascertained to the genome by where they get aligned. On the other hand, in de-novo assembly, assembler looks for overlaps between reads to figure out their relative positions. Due to the fact that there are numerous such possibilities of overlap, the latter method is more computationally-intensive than the former.

# Methods: 

# Reference-guided Assembly:
Quality Trimmed reads of Aiptasia genome obtained from GMAP database were aligned, sorted into SAM files and converted into BAM files followed by indexing of the alignments such that they can be searched more quickly. The BAM files are used to assemble a reference-guided transcriptome.

## Merge BAM Files-
Trinity is the tool used to perform reference-guided assembly. For this samtools is used to merge all the BAM files and the code is run for a genome guided assembly. After the completion of the run a fasta file is generated with the transcriptome assembly.

## Checking output statistics-
The output statistics of transcriptome are determined by studying the size of the assembled contigs. N10-N50 indicate the length of the assemblies. The contigs are first sorted from longest to shortest. This then moves the horizontal line until 50% of all assembled bases are above and and the other 50% are below it. Ideally they should match the length of the original transcripts but there are chances of multiple regions occurring wherein the assembler was not able to find enough overlap between the short reads to link them that could be assembled. 

# De-Novo Transcriptome Assembly-
This process requires two comma-separated lists of the left and right reads . Thus lists of left and rght reads are built and then trinity de-novo assembly command is run.

# Checking Assembly Statistics-
De-Novo Assembly statistics are determined by studying the length of the contigs. The scripts enlists lengths of N10-N50, median contig length, average contig length and also the total assembled bases.

The two assembled transcriptomes hence generated are then pushed into github repository.
