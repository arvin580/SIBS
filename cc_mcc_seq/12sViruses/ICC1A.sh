cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping/1A/1A.bam |python 1.filter.py >ICC1A.unmapped
python 2.fq.py ICC1A.unmapped

read1fq=ICC1A.unmapped.fq
read1sai=ICC1A.unmapped.sai
bam=ICC1A.unmapped.bam
sam=ICC1A.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/1-mapping

bwa aln -I \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
-r "@RG\tID:1a\tSM:1a\tLB:1a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM


