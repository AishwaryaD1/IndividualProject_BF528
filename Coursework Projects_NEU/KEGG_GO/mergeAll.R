#!/usr/bin/env Rscript
# mergeAll.R

# Load BLAST results as a table using tab (\t) as separator.
blast <- read.table("../BLAST/alignPredicted.txt", sep="\t", header=FALSE)

# Set column names to match fields selected in BLAST
colnames(blast) <- c("qseqid", "sacc", "qlen", "slen", "length", "nident", "pident", "evalue", "stitle")

# Calculate coverage as nident/slen
blast$cov <- blast$nident/blast$slen

# Select only blast rows which have coverage greater than .9
blast <- subset(blast, cov > .9, select = -c(stitle))

# Read kegg.txt, produced by get_kegg_ids, as a table
kegg <- read.table("kegg.txt", sep="\t", header=FALSE, fill = T)

# Set the column names for kegg
colnames(kegg) <- c("sacc", "kegg")

# subject accession (sacc)
kegg$sacc <- gsub("up:", "", kegg$sacc)

# Merge the tables
blast_kegg <- merge(blast, kegg)

# Display the first few lines of output
head(blast_kegg)
go <- read.csv("sp_go.txt", fill = T, sep="\t", header=FALSE)
head(go)

kegg <- read.table("kegg.txt", fill = T, sep="\t", header=F)
colnames(kegg) <- c("sacc", "kegg")

ko <- read.table("ko.txt", fill = T, sep="\t", header = F)
colnames(ko) <- c("kegg", "ko")

path <- read.table("path.txt", fill = T, sep="\t", header = F)
colnames(path) <- c("ko", "path")

getPath <- read.table("ko", fill = T, sep="\t", header = F)
colnames(getPath) <- c("path", "pathway")

r1<- merge(kegg, ko)
r2<- merge(r1, path)
r3<- merge(r2, getPath)

head(r3)


