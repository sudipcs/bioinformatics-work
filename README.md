### 1. interleaved2single.py
An interleaved fastq file containing paired-end reads needs to be split into two separate files, one for each read, for some applications to process them further. The python code for this command produces two valid fastq files separating the two reads. <br>
**Run:** - python interleaved2single.py –i interleaved.fq –1 read1.fq –2 read2.fq

 ### 2. Analysis of transposable elements (TEs)
 Analyzing transposable elements (TEs) from FASTQ files involves extracting sequence lengths and calculating GC content.
 
 TE_GCanalysis.py provides a function to calculate the GC content of a sequence. seq_length.py checks a sequence within an FASTA file and TE sequence pattern, it reads sequences from a FASTA file and identifies TE sequences.

 TE_analysis.py or notebook 1. read the FASTQ file, calculate the sequence length and GC content for each read, and then print the average sequence length and average GC content. 2. also it checks if any of the transposable elements are present. If a match is found, it prints the sequence ID and the sequence containing the transposable element.

### 3. Analysis of transcriptome features
Given a GTF file, develop a Python script to extract and save the transcriptome features into individual BED files.
GTF: ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_33/gencode.v33.annotation.gtf.gz


