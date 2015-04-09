#!/bin/bash

cd /netshare1/home1/szzhongxin/proj1/hansun/annotation

#perl annovar/convert2annovar.pl --format vcf4 --includeinfo snpindel_snp3030_raw.snp.recalibrated.vcf >snpindel_snp3030_raw.snp.recalibrated.annovar
#perl annovar/convert2annovar.pl --format vcf4 --includeinfo snpindel2_snp3030_raw.snp.recalibrated.vcf >snpindel2_snp3030_raw.snp.recalibrated.annovar

#perl annovar/annotate_variation.pl -geneanno snpindel_snp3030_raw.snp.recalibrated.annovar  annovar/humandb/ --buildver hg19 
#perl annovar/annotate_variation.pl -geneanno snpindel2_snp3030_raw.snp.recalibrated.annovar  annovar/humandb/ --buildver hg19 

#perl annovar/summarize_annovar.pl raw.snp.annovar annovar/humandb --buildver hg19 >raw.snp.annotation

perl annovar/convert2annovar.pl --format vcf4 --includeinfo snpindel_indel3030_raw.indel.recalibrated.vcf >snpindel_indel3030_raw.indel.recalibrated.annovar
perl annovar/convert2annovar.pl --format vcf4 --includeinfo snpindel2_indel3030_raw.indel.recalibrated.vcf >snpindel2_indel3030_raw.indel.recalibrated.annovar

perl annovar/annotate_variation.pl -geneanno snpindel_indel3030_raw.indel.recalibrated.annovar  annovar/humandb/ --buildver hg19 
perl annovar/annotate_variation.pl -geneanno snpindel2_indel3030_raw.indel.recalibrated.annovar  annovar/humandb/ --buildver hg19 

