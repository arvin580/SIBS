cd /netshare1/home1/szzhongxin/proj1/hansun/samtools/CHC5

samtools mpileup -uD6f /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta /netshare1/home1/szzhongxin/proj1/hansun/mapping2/5A/5A.bam | bcftools view -bvcg - > var.raw.chc5a.bcf
bcftools view var.raw.chc5a.bcf | vcfutils.pl varFilter -D 100 > var.chc5a.flt.vcf 
samtools mpileup -uD6f /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta /netshare1/home1/szzhongxin/proj1/hansun/mapping4/5B/5B.bam | bcftools view -bvcg - > var.raw.chc5b.bcf
bcftools view var.raw.chc5b.bcf | vcfutils.pl varFilter -D 100 > var.chc5b.flt.vcf 
