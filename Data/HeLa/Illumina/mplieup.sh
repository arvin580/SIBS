cd  /netshare1/home1/people/hansun/Data/Lundberg/Illumina

samtools mpileup -uDf /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta ERR0498-04-05.bam > tmp.raw.bcf
bcftools view -bvcg tmp.raw.bcf > var.raw.bcf
bcftools view var.raw.bcf | vcfutils.pl varFilter > var.flt.vcf 
