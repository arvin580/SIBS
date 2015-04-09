#!/bin/bash

cd /netshare1/home1/szzhongxin/proj1/hansun/ANNOVAR

#perl annovar/convert2annovar.pl --format vcf4 --includeinfo snpindel_snp3030_raw.snp.recalibrated.vcf >snpindel_snp3030_raw.snp.recalibrated.annovar
#perl annovar/convert2annovar.pl --format vcf4 --includeinfo snpindel2_snp3030_raw.snp.recalibrated.vcf >snpindel2_snp3030_raw.snp.recalibrated.annovar

#perl annovar/convert2annovar.pl --format vcf4 --includeinfo snpindel_indel3030_raw.indel.recalibrated.vcf >snpindel_indel3030_raw.indel.recalibrated.annovar
#perl annovar/convert2annovar.pl --format vcf4 --includeinfo snpindel2_indel3030_raw.indel.recalibrated.vcf >snpindel2_indel3030_raw.indel.recalibrated.annovar


#perl annovar/convert2annovar.pl --format vcf4 --includeinfo snp3/snpindel3_snp3030_raw.snp.recalibrated.vcf >snp3/snpindel3_snp3030_raw.snp.recalibrated.annovar
#perl annovar/convert2annovar.pl --format vcf4 --includeinfo indel3/snpindel3_indel3030_raw.indel.recalibrated.vcf >indel3/snpindel3_indel3030_raw.indel.recalibrated.annovar

#perl annovar/annotate_variation.pl -downdb gene annovar/humandb/ -buildver hg19
#perl annovar/annotate_variation.pl -downdb avsift  annovar/humandb/ -buildver hg19
#perl annovar/annotate_variation.pl -downdb genomicSuperDups  annovar/humandb/ -buildver hg19
#perl annovar/annotate_variation.pl -downdb snp131   annovar/humandb/ -buildver hg19
#perl annovar/annotate_variation.pl -downdb -webfrom annovar snp135   annovar/humandb/ -buildver hg19
#perl annovar/annotate_variation.pl -downdb -webfrom annovar ljb_all   annovar/humandb/ -buildver hg19
#perl annovar/annotate_variation.pl -downdb -webfrom annovar esp_5400_all   annovar/humandb/ -buildver hg19
###lperl annovar/annotate_variation.pl -downdb ALL.sites.2010_11   annovar/humandb/ -buildver hg19
#perl annovar/annotate_variation.pl -downdb phastConsElements46way   annovar/humandb/ -buildver hg19
#perl annovar/annotate_variation.pl -downdb -webfrom annovar 1000g2012feb annovar/humandb/ -buildver hg19


#perl annovar/annotate_variation.pl -geneanno snpindel_snp3030_raw.snp.recalibrated.annovar  annovar/humandb/ --buildver hg19 
#perl annovar/annotate_variation.pl -geneanno snpindel2_snp3030_raw.snp.recalibrated.annovar  annovar/humandb/ --buildver hg19 


#perl annovar/annotate_variation.pl -geneanno snpindel_indel3030_raw.indel.recalibrated.annovar  annovar/humandb/ --buildver hg19 
#perl annovar/annotate_variation.pl -geneanno snpindel2_indel3030_raw.indel.recalibrated.annovar  annovar/humandb/ --buildver hg19 



#perl annovar/summarize_annovar.pl snp/snpindel_snp3030_raw.snp.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile sum_snp
#perl annovar/summarize_annovar.pl snp2/snpindel2_snp3030_raw.snp.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile sum_snp2
#perl annovar/summarize_annovar.pl indel/snpindel_indel3030_raw.indel.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile sum_indel
#perl annovar/summarize_annovar.pl indel2/snpindel2_indel3030_raw.indel.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile sum_indel2

#perl annovar/summarize_annovar.pl snp3/snpindel3_snp3030_raw.snp.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile snp3/sum_snp3
#perl annovar/summarize_annovar.pl indel3/snpindel3_indel3030_raw.indel.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile indel3/sum_indel3


#perl annovar/auto_annovar.pl -model recessive snp/snpindel_snp3030_raw.snp.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile auto_snp
#perl annovar/auto_annovar.pl -model recessive snp2/snpindel2_snp3030_raw.snp.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile auto_snp2
#perl annovar/auto_annovar.pl -model recessive indel/snpindel_indel3030_raw.indel.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile auto_indel
#perl annovar/auto_annovar.pl -model recessive indel2/snpindel2_indel3030_raw.indel.recalibrated.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile auto_indel2


#perl annovar/convert2annovar.pl --format vcf4 --includeinfo snv16s/var.flt.vcf >snv16s/snv16s.var.flt.annovar
#perl annovar/summarize_annovar.pl snv16s/snv16s.var.flt.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile snv16s/sum_snv16s


#perl annovar/convert2annovar.pl --format vcf4 --includeinfo snv16sExome/var.flt.vcf >snv16sExome/snv16sExome.var.flt.annovar
#perl annovar/summarize_annovar.pl snv16sExome/snv16sExome.var.flt.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile snv16sExome/sum_snv16sExome

#perl annovar/convert2annovar.pl --format vcf4 --includeinfo Lundberg-Illumina/var.flt.vcf >Lundberg-Illumina/var.flt.annovar
#perl annovar/summarize_annovar.pl Lundberg-Illumina/var.flt.annovar annovar/humandb --buildver hg19  --verdbsnp 135 --ver1000g 1000g2012feb -outfile Lundberg-Illumina/sum_snv


perl annovar/annotate_variation.pl -downdb -webfrom annovar snp137   annovar/humandb/ -buildver hg19
