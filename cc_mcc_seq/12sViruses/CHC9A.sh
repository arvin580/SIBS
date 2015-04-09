cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping2/9A/9A.bam |python 1.filter.py >CHC9A.unmapped
python 2.fq.py CHC9A.unmapped

read1fq=CHC9A.unmapped.fq
read1sai=CHC9A.unmapped.sai
bam=CHC9A.unmapped.bam
sam=CHC9A.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/1-mapping

bwa aln -I \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
-r "@RG\tID:m9a\tSM:m9a\tLB:m9a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM


