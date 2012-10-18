#!/bin/bash
### Job name
#LJRS -N rna_seq 
### Queue name 
#LJRS -q dpool
### Number of nodes 
#LJRS -l nodes=2:ppn=4
 
# This job's working directory
cd 

bowtie -a --best --strata -v 2 tte/genome/tte -1 tte/55c/100527_I125_FC2027GABXX_L3_THEcwvTARAAPEI-4_1.fq -2 tte/55c/100527_I125_FC2027GABXX_L3_THEcwvTARAAPEI-4_2.fq -S tte55.sam 
bowtie -a --best --strata -v 2 tte/genome/tte -1 tte/65c/100527_I125_FC2027GABXX_L3_THEcwvTBRAAPEI-5_1.fq -2 tte/65c/100527_I125_FC2027GABXX_L3_THEcwvTBRAAPEI-5_2.fq -S tte65.sam 
bowtie -a --best --strata -v 2 tte/genome/tte -1 tte/75c/100527_I125_FC2027GABXX_L4_THEcwvTCRAAPEI-6_1.fq -2 tte/75c/100527_I125_FC2027GABXX_L4_THEcwvTCRAAPEI-6_2.fq -S tte75.sam 
bowtie -a --best --strata -v 2 tte/genome/tte -1 tte/80c/T8-100606_I125_FC20260ABXX_L4_THEjhdTARAAPEI-7_1.fq -2 tte/80c/T8-100606_I125_FC20260ABXX_L4_THEjhdTARAAPEI-7_2.fq -S tte80.sam 



###perl code/filtersam.pl tte55.sam tte55valid.sam tte55invalid.sam
###perl code/filtersam.pl tte65.sam tte65valid.sam tte65invalid.sam
###perl code/filtersam.pl tte75.sam tte75valid.sam tte75invalid.sam
###perl code/filtersam.pl tte80.sam tte80valid.sam tte80invalid.sam



samtools view -bS -o tte55.bam tte55.sam 
samtools view -bS -o tte65.bam tte65.sam 
samtools view -bS -o tte75.bam tte75.sam 
samtools view -bS -o tte80.bam tte80.sam 

samtools sort tte55.bam tte55sorted
samtools sort tte65.bam tte65sorted
samtools sort tte75.bam tte75sorted
samtools sort tte80.bam tte80sorted


samtools pileup -f tte/genome/NC_003869.fna  tte55sorted.bam  >tte55pileup
samtools pileup -f tte/genome/NC_003869.fna  tte65sorted.bam  >tte65pileup
samtools pileup -f tte/genome/NC_003869.fna  tte75sorted.bam  >tte75pileup
samtools pileup -f tte/genome/NC_003869.fna  tte80sorted.bam  >tte80pileup
