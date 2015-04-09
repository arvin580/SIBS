cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping6/10A/10A.bam |python 1.filter.py >CHC10A.unmapped
python 2.fq.py CHC10A.unmapped

read1fq=CHC10A.unmapped.fq
read1sai=CHC10A.unmapped.sai
bam=CHC10A.unmapped.bam
sam=CHC10A.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/1-mapping

bwa aln -I \
	        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
		        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
			        >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
-r "@RG\tID:10a\tSM:10a\tLB:4a\tPL:illumina\tPU:barcode" > $sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM

