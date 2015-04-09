cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping2/4A/4A.bam |python 1.filter.py >CHC4A.unmapped
python 2.fq.py CHC4A.unmapped

read1fq=CHC4A.unmapped.fq
read1sai=CHC4A.unmapped.sai
bam=CHC4A.unmapped.bam
sam=CHC4A.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/1-mapping

bwa aln -I \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
-r "@RG\tID:m4a\tSM:m4a\tLB:m4a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM


