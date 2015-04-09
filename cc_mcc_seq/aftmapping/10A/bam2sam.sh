cd /netshare1/home1/szzhongxin/proj1/hansun/aftmapping/10A 
#samtools view -h -o 10A.realigned.test.sam 10A.realigned.bam
/netshare1/home1/people/hansun/MySoft/samtools/samtools-0.1.16/samtools view -bS -o 10A.realigned.test.bam 10A.realigned.test.sam
/netshare1/home1/people/hansun/MySoft/samtools/samtools-0.1.16/samtools index 10A.realigned.test.bam 
md5sum 10A.realigned.test.bam
md5sum 10A.realigned.bam
md5sum 10A.realigned.test.bai
md5sum 10A.realigned.bai

