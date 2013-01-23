cd  /netshare1/home1/people/hansun/Data 
bowtie -p 8 --sam --best -C -v 2 peptide2dna/peptide2dna  Lundberg/SRR040290.fastq -S peptide2dna_SRR040290_m_v.sam --un peptide2dna_SRR040290_un_v 
###samtools view -bS -o SRR040290.bam  SRR040290.sam 
###samtools sort SRR040290.bam SRR040290sorted 
###samtools pileup -f tte/genome/NC_003869.fna  tte55sorted.bam  >tte55pileup






