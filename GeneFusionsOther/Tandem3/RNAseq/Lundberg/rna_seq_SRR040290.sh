#!/bin/bash
### Job name
#LJRS -N rna_seq 
### Queue name 
#LJRS -q dpool
### Number of nodes 
#LJRS -l nodes=2:ppn=4
 
### This job's working directory
cd  /netshare1/home1/people/hansun/Data 
bowtie -p 8 --sam --best -C -v 2 h_sapiens_37_asm_c/h_sapiens_37_asm_c  Lundberg/SRR040290.fastq -S SRR040290_m_v.sam --un SRR040290_un_v 
###samtools view -bS -o SRR040290.bam  SRR040290.sam 
###samtools sort SRR040290.bam SRR040290sorted 
###samtools pileup -f tte/genome/NC_003869.fna  tte55sorted.bam  >tte55pileup






