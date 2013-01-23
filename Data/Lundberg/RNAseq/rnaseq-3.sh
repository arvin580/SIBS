cd   /netshare1/home1/people/hansun/Data/Lundberg/RNAseq
bowtie -p 8 --sam -C  /netshare1/home1/people/hansun/Data/GenomeSeq/Human/bowtie/hg19.c  SRR040361.fastq -S SRR040361.sam 
###samtools view -bS -o SRR040290.bam  SRR040290.sam 
###samtools sort SRR040290.bam SRR040290sorted 
###samtools pileup -f tte/genome/NC_003869.fna  tte55sorted.bam  >tte55pileup






