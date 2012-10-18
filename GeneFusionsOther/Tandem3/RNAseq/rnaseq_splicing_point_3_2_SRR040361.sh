#!/bin/bash
### Job name
#LJRS -N rna_seq 
### Queue name 
#LJRS -q dpool
### Number of nodes 
#LJRS -l nodes=2:ppn=4
 
### This job's working directory
cd /netshare1/home1/people/hansun/GeneFusionsOther/Tandem3/RNAseq
bowtie -p 8 --sam --best -C -v 2 /netshare1/home1/people/hansun/GeneFusionsOther/Tandem3/RNAseq/splicing_point/splicing_point_3_2 /netshare1/home1/people/hansun/Data/Lundberg/RNAseq/SRR040361.fastq -S splicing_point_3_2_SRR040361_v.sam 
###samtools view -bS -o SRR040290.bam  SRR040290.sam 
###samtools sort SRR040290.bam SRR040290sorted 
###samtools pileup -f tte/genome/NC_003869.fna  tte55sorted.bam  >tte55pileup






