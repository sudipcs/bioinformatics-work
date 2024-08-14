### 1. interleaved2single.py
An interleaved fastq file containing paired-end reads needs to be split into two separate files, one for each read, for some applications to process them further. The python code for this command produces two valid fastq files separating the two reads. <br>
**Run:** - python interleaved2single.py –i interleaved.fq –1 read1.fq –2 read2.fq

 ### 2. Analysis of transposable elements (TEs)
 Analyzing transposable elements (TEs) from FASTQ files involves extracting sequence lengths and calculating GC content.
 
 TE_GCanalysis.py provides a function to calculate the GC content of a sequence. seq_length.py checks a sequence within an FASTA file and TE sequence pattern, it read sequences from a FASTA file and identifies TE sequences.


