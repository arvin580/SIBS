cd /netshare1/home1/szzhongxin/proj1/hansun/CNV/cnv-seq 

samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping/9A/9A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_9A.hits


