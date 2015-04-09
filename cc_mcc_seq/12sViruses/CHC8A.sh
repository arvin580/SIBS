cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping2/8A/8A.bam |python 1.filter.py >CHC8A.unmapped
python 2.fq.py CHC8A.unmapped

read1fq=CHC8A.unmapped.fq
read1sai=CHC8A.unmapped.sai
bam=CHC8A.unmapped.bam
sam=CHC8A.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/1-mapping

bwa aln -I \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
-r "@RG\tID:m8a\tSM:m8a\tLB:m8a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM


