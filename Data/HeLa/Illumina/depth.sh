cd  /netshare1/home1/people/hansun/Data/Lundberg/Illumina

samtools mpileup -uf /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta ERR0498-04-05.bam |bcftools view - > ERR0498-04-05.mpileup
