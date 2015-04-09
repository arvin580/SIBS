cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping6/7A/7A.bam |python 1.filter.py >CHC7A.unmapped
python 2.fq.py CHC7A.unmapped

read1fq=CHC7A.unmapped.fq
read1sai=CHC7A.unmapped.sai
bam=CHC7A.unmapped.bam
sam=CHC7A.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/1-mapping

bwa aln -I \
	        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
	        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
			        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
-r "@RG\tID:m7a\tSM:m7a\tLB:m7a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM

