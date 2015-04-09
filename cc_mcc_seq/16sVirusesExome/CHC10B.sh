cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping8/10B/10B.bam |python 1.filter.py >CHC10B.unmapped
python 2.fq.py CHC10B.unmapped

read1fq=CHC10B.unmapped.fq
read1sai=CHC10B.unmapped.sai
bam=CHC10B.unmapped.bam
sam=CHC10B.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/1-mapping

bwa aln -I \
                /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
                        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
                                >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
-r "@RG\tID:m10b\tSM:m10b\tLB:m10b\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM

