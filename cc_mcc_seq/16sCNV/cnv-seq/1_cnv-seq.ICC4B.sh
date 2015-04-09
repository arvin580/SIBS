cd  /netshare1/home1/szzhongxin/proj1/hansun/16sCNV/cnv-seq

samtools view -F 4  /netshare1/home1/szzhongxin/proj1/hansun/mapping7/4B/4B.bam | perl -lane 'print "$F[2]\t$F[3]"' > ICC_4B.hits

