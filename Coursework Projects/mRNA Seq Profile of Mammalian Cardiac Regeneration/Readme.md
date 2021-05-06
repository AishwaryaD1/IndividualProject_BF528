# Project Description

A brief description of what this repository is for and what it contains

# Contributors

Names: Konrad Thorner, Aishwarya Deengar, Jia Liu, Morgan Rozman

Github: kthorner, AishwaryaD1, jialiu0103, morganroz

Email: kthorner@bu.edu, adeengar@bu.edu , jiliu@bu.edu, mrozman@bu.edu

# Repository Contents

## run_tophat.qsub
Qsub file to run the commands on the scc. Includes the command to run tophat alignment of the reads from the P0_1 sample fastq files. Outputs alignment data, including accepted_hits.bam.

## run_genebody.qsub
Runs the geneBody_coverage.py program from the RSeQC package on the accepted_hits.bam file output from the tophat analysis done in the run_tophat.qsub code. Outputs a text file of coverage statistics for the alignments. In a qsub file to run on the scc.

## run_cufflinks.qsub
Runs cufflinks on the accepted_hits.bam file output from run_tophat.qsub. Cufflinks will count how reads map to genomic regions defined by the mm9 reference. Outputs genes.fpkm_tracking file which contains the quantified alignments in FPKM (fragments per kilobase of exon model per million reads mapped) for all genes.

## run_cuffdiff.qsub
Runs cuffdiff on the P0_1, P0_2, Ad_1, and Ad_2 samples to identify differentially expressed genes between the samples and the mm9 reference. Outputs the gene_exp.diff file with differential expression data for all genes.

## Analyst
Obtained the differential gene expression of the two conditions (P0 and A) and sorted the data frame so that the smallest q_values are at the top. Produced a table of the top ten differentially expressed genes. Produced a histogram of the log2.foldchange column for all genes. Created a new data frame that contains only the significant genes. Created a second histogram of the log2 fold change values only for significant genes. Created two separate data frames with only the up- and down-regulated genes using the log2.foldchange column. Included the count of up and down regulated genes. Finally, wrote out the up- and down- regulated gene names to separate csv files for subsequent DAVID Analysis.
