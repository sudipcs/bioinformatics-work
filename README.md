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

Task 1: Given the GTF file, **analysis_transcriptome_feature.py** script to extract and save the
following transcriptome features into individual BED files. 
• Genes: Include both gene ID and name.
• Transcripts: Include transcript ID, gene ID, and gene name.
• Coding exons, 5' UTRs, 3' UTRs, and introns: Annotate each with associated gene names and/or transcript IDs/names, as applicable.

Also using the external BED file (T1.bed), map and match its regions to the features extracted above. Save the results in a separate file and append a column indicating the corresponding feature type (e.g., exon, 5UTR, 3UTR, intron, and UN for non-mapped).



