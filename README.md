### 1. interleaved2single.py
An interleaved fastq file containing paired-end reads needs to be split into two separate files, one for each read, for some applications to process them further. The python code for this command produces two valid fastq files separating the two reads. <br>
**Run:** - python interleaved2single.py –i interleaved.fq –1 read1.fq –2 read2.fq

 ### 2. Analysis of transposable elements (TEs)
 Analyzing transposable elements (TEs) from FASTQ files involves extracting sequence lengths and calculating GC content.
 
 TE_GCanalysis.py provides a function to calculate the GC content of a sequence. seq_length.py checks a sequence within an FASTA file and TE sequence pattern, it reads sequences from a FASTA file and identifies TE sequences.

 TE_analysis.py or notebook 1. read the FASTQ file, calculate the sequence length and GC content for each read, and then print the average sequence length and average GC content. 2. also it checks if any of the transposable elements are present. If a match is found, it prints the sequence ID and the sequence containing the transposable element.

### 3. Analysis of transcriptome features
Given a GTF file, develop a Python script to extract and save the transcriptome features into individual BED files.

Input GTF: ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_33/gencode.v33.annotation.gtf.gz (Download and save it to local folder path)

Given the GTF file, **analysis_transcriptome_feature.py** script to extract and save the following transcriptome features into individual BED files. <br>
• Genes: Include both gene ID and name. <br>
• Transcripts: Include transcript ID, gene ID, and gene name. <br>
• Coding exons, 5' UTRs, 3' UTRs, and introns: Annotate each with associated gene names and/or transcript IDs/names, as applicable. <br>

Also using the external BED file (T1.bed), map and match its regions to the features extracted above. Save the results in a separate file and append a column indicating the corresponding feature type (e.g., exon, 5UTR, 3UTR, intron, and UN for non-mapped).

### 4. Cluster genes based on their expression

Given a matrix where rows represent genes and columns represent samples, 
Attached are two matrices T3_M1.txt and T3_M2.txt. Perform statistical tests to test for differences/similarity between any two matrices by preserving the matrix structure?
develop a Python to: Use the attached T2.txt file as input. <br>
• Cluster genes based on their expression patterns across samples. <br>
• Visualize the representative expression profile for each identified cluster. <br>
• Do the inverse, i.e., cluster samples based and plot gene signatures. <be>

**cluster_genes_exp.py or notebook** cluster genes based on their expression patterns across samples. Visualize the representative expression profile for each identified cluster.

### 5. Cluster genes using principal component analysis (PCA)

Data: <br>
a. GeneCounts.txt - This file contains gene count information for 24 samples from a bulk RNAseq experiment, with columns indicating sample IDs and rows indicating gene IDs. <br>
b. genelist.txt - This file contains 200 gene IDs. <br>

(1) Use the `genelist.txt` information to subset the gene count information from `GeneCounts.txt` (i.e. retrieve only the GeneCounts.txt data for the genes in genelist.txt.
(2) Subset the gene count information from (1) further by removing all genes that have 0 counts for all of their samples.
(3) Sample 1-12 are experimental subjects from the control group and Samples 13-24 are experimental subjects from the treatment group. Apply principal component analysis (PCA
on the list from (2) and plot PC1 vs PC2 for all samples, and make sure the plot contains the following information:
  a. Proportion of variance explained by PC 1 and PC 2 each
  b. Data points are colored according to whether they represent "control" or "treatment" data.

