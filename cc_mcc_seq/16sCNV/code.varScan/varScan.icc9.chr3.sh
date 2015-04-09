cd /netshare1/home1/szzhongxin/proj1/hansun/16sCNV
varscan=/netshare1/home1/people/hansun/MySoft/VarScan/VarScan.v2.3.3.jar
hg19=/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta

ICC4A=/netshare1/home1/szzhongxin/proj1/hansun/mapping5/4A/4A.bam
ICC5A=/netshare1/home1/szzhongxin/proj1/hansun/mapping5/5A/5A.bam
ICC9A=/netshare1/home1/szzhongxin/proj1/hansun/mapping5/9A/9A.bam
ICC10A=/netshare1/home1/szzhongxin/proj1/hansun/mapping5/10A/10A.bam

CHC5A=/netshare1/home1/szzhongxin/proj1/hansun/mapping6/5A/5A.bam
CHC6A=/netshare1/home1/szzhongxin/proj1/hansun/mapping6/6A/6A.bam
CHC7A=/netshare1/home1/szzhongxin/proj1/hansun/mapping6/7A/7A.bam
CHC10A=/netshare1/home1/szzhongxin/proj1/hansun/mapping6/10A/10A.bam


ICC4B=/netshare1/home1/szzhongxin/proj1/hansun/mapping7/4B/4B.bam
ICC5B=/netshare1/home1/szzhongxin/proj1/hansun/mapping7/5B/5B.bam
ICC9B=/netshare1/home1/szzhongxin/proj1/hansun/mapping7/9B/9B.bam
ICC10B=/netshare1/home1/szzhongxin/proj1/hansun/mapping7/10B/10B.bam

CHC5B=/netshare1/home1/szzhongxin/proj1/hansun/mapping8/5B/5B.bam
CHC6B=/netshare1/home1/szzhongxin/proj1/hansun/mapping8/6B/6B.bam
CHC7B=/netshare1/home1/szzhongxin/proj1/hansun/mapping8/7B/7B.bam
CHC10B=/netshare1/home1/szzhongxin/proj1/hansun/mapping8/10B/10B.bam

chr=chr3
sample=ICC9



samtools mpileup -q 1 -f $hg19 -r $chr $ICC9B $ICC9A | \
java -jar $varscan copynumber - varScan.${sample}.${chr} --mpileup 1


java -jar $varscan copyCaller varScan.${sample}.${chr}.copynumber --output-file varScan.${sample}.${chr}.copynumber.called

