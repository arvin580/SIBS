#!/bin/bash
### Job name
#LJRS -N rna_seq 
### Queue name 
#LJRS -q dpool
### Number of nodes 
#LJRS -l nodes=2:ppn=4
 
### This job's working directory
cd  /netshare1/home1/people/hansun/Data 
bowtie -p 8 --sam --best -C -v 2 h_sapiens_37_asm_c/h_sapiens_37_asm_c  Lundberg/SRR040293.fastq -S SRR040293_m_v.sam  --un SRR040293_un_v
###samtools view -bS -o SRR040293.bam  SRR040293.sam 
###samtools sort SRR040293.bam SRR040293sorted 
###samtools pileup -f tte/genome/NC_003869.fna  tte55sorted.bam  >tte55pileup






