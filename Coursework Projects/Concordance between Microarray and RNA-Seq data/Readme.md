# Project Description

Code for BF528 Project 3: Concordance of microarray and RNA-Seq differential gene expression

# Contributors

Names: Konrad Thorner, Aishwarya Deengar, Jia Liu, Morgan Rozman

Github: kthorner, AishwaryaD1, jialiu0103, morganroz

Email: kthorner@bu.edu, adeengar@bu.edu , jiliu@bu.edu, mrozman@bu.edu

# Repository Contents

## run_limma.R
Limma analysis for microarray data for each chemical group. This code utilizes a sample information data set and an RNA normalized matrix of all experiments. Outputs csv files of expression for each chemical group.

## create_fc_plots.R
Creates a histogram of significant probesets for each chemical group and volcano plots for each chemical group.

## concordence.R
Computes concordance between microarray and RNA-Seq data. Also creates scatter plots and histograms for concordance analyses.

## heatmap.R
Creates a heatmap of normalized counts for all samples
