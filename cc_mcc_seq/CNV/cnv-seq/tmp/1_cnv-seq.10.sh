cd /netshare1/home1/szzhongxin/proj1/hansun/CNV/cnv-seq 


samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping3/4B/4B.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_4B.hits
