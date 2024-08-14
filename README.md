## interleaved2single.py
An interleaved fastq file containing paired-end reads needs to be split into two separate files, one for each read, for some applications to process them further. The python code for this command produces two valid fastq files separating the two reads. 
**Run:** - python interleaved2single.py –i interleaved.fq –1 read1.fq –2 read2.fq



