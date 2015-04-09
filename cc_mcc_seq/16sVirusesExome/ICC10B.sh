cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping7/10B/10B.bam |python 1.filter.py >ICC10B.unmapped
python 2.fq.py ICC10B.unmapped

read1fq=ICC10B.unmapped.fq
read1sai=ICC10B.unmapped.sai
bam=ICC10B.unmapped.bam
sam=ICC10B.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/1-mapping

bwa aln -I \
	        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
		        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
			        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
-r "@RG\tID:4a\tSM:4a\tLB:4a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM

