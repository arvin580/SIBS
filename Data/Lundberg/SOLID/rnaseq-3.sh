cd   /netshare1/home1/people/hansun/Data/Lundberg/RNAseq
sample=SRR040361
bowtie -p 8 --sam -C  /netshare1/home1/people/hansun/Data/GenomeSeq/Human/bowtie/hg19.c  $sample.fastq -S $sample.sam 
samtools view -bS -o $sample.bam $sample.sam
samtools  sort $sample.bam $sample.sorted
mv $sample.sorted.bam $sample.bam
samtools index $sample.bam
samtools  flagstat $sample.bam >$sample.stat


