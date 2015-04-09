cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping/8A/8A.bam |python 1.filter.py >ICC8A.unmapped
python 2.fq.py ICC8A.unmapped

read1fq=ICC8A.unmapped.fq
read1sai=ICC8A.unmapped.sai
bam=ICC8A.unmapped.bam
sam=ICC8A.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/1-mapping

bwa aln -I \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
        /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/12sViruses/$read1fq \
-r "@RG\tID:8a\tSM:8a\tLB:8a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM


