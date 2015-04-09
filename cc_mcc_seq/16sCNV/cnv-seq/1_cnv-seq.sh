cd  /netshare1/home1/szzhongxin/proj1/hansun/16sCNV/cnv-seq

samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping5/10A/10A.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_10A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping5/4A/4A.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_4A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping5/5A/5A.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_5A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping5/9A/9A.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_9A.hits


samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping6/10A/10A.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_10A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping6/5A/5A.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_5A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping6/6A/6A.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_6A.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping6/7A/7A.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_7A.hits


samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping7/10B/10B.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_10B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping7/4B/4B.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_4B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping7/5B/5B.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_5B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping7/9B/9B.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_9B.hits

samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping8/10B/10B.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_10B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping8/5B/5B.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_5B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping8/6B/6B.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_6B.hits
samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping8/7B/7B.bam | perl -lane 'print "$F[2]\t$F[3]"' > CHC_7B.hits


