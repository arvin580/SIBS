cd /netshare1/home1/szzhongxin/proj1/hansun/viruses
#samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping4/5B/5B.bam |python 1.filter.py >CHC5B.unmapped
#python 2.fq.py CHC5B.unmapped

read1fq=CHC5B.unmapped.fq
read1sai=CHC5B.unmapped.sai
bam=CHC5B.unmapped.bam
sam=CHC5B.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/viruses/mapping

bwa aln -I \
	        /netshare1/home1/szzhongxin/proj1/hansun/viruses/bwa/viruses \
		        /netshare1/home1/szzhongxin/proj1/hansun/viruses/$read1fq \
			        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/viruses/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/viruses/$read1fq \
-r "@RG\tID:4a\tSM:4a\tLB:4a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM

