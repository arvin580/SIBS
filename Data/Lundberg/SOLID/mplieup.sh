cd  /netshare1/home1/people/hansun/Data/Lundberg/RNAseq

samtools mpileup -uDf /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta SRR040290.bam SRR040293.bam SRR040361.bam > tmp.raw.bcf
bcftools view -bvcg tmp.raw.bcf > var.raw.bcf
bcftools view var.raw.bcf | vcfutils.pl varFilter > var.flt.vcf 
