cd /netshare1/home1/people/hansun/Project/LianBaoFeng
varscan=/netshare1/home1/people/hansun/MySoft/VarScan/VarScan.v2.3.3.jar
hg19=/netshare1/home1/people/hansun/Project/LianBaoFeng/hg19.fa

P1=/netshare1/home1/people/hansun/Project/LianBaoFeng/p1.rmdup.bam
B1=/netshare1/home1/people/hansun/Project/LianBaoFeng/b1.rmdup.bam
N1=/netshare1/home1/people/hansun/Project/LianBaoFeng/n1.rmdup.bam
J1=/netshare1/home1/people/hansun/Project/LianBaoFeng/j1.rmdup.bam
W1=/netshare1/home1/people/hansun/Project/LianBaoFeng/w1.rmdup.bam

sample=P1J1
chr=chrY

samtools mpileup -q 1 -f $hg19 -r $chr $J1 $P1 | \
java -jar $varscan copynumber - varScan.${sample}.${chr} --mpileup 1


java -jar $varscan copyCaller varScan.${sample}.${chr}.copynumber --output-file varScan.${sample}.${chr}.copynumber.called

