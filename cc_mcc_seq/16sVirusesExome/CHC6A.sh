cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping6/6A/6A.bam |python 1.filter.py >CHC6A.unmapped
python 2.fq.py CHC6A.unmapped

read1fq=CHC6A.unmapped.fq
read1sai=CHC6A.unmapped.sai
bam=CHC6A.unmapped.bam
sam=CHC6A.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/1-mapping

bwa aln -I \
	        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
		        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
			        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
-r "@RG\tID:m6a\tSM:m6a\tLB:m6a\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM

