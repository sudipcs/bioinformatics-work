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

**cluster_genes_exp.py** Cluster genes based on their expression patterns across samples. Visualize the representative expression profile for each identified cluster.


