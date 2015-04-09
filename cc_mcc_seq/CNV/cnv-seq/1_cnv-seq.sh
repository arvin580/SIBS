cd /netshare1/home1/szzhongxin/proj1/hansun/CNV/cnv-seq 

samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping/10A/10A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_10A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping/4A/4A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_4A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping/5A/5A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_5A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping/9A/9A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_9A.hits


samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping2/10A/10A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_10A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping2/5A/5A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_5A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping2/6A/6A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_6A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping2/7A/7A.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_7A.hits


samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping3/10B/10B.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_10B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping3/4B/4B.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_4B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping3/5B/5B.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_5B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping3/9B/9B.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_9B.hits

samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping4/10B/10B.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_10B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping4/5B/5B.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_5B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping4/6B/6B.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_6B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/aftmapping4/7B/7B.realigned.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_7B.hits


