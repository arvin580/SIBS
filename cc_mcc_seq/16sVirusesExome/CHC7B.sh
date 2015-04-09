cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping8/7B/7B.bam |python 1.filter.py >CHC7B.unmapped
python 2.fq.py CHC7B.unmapped

read1fq=CHC7B.unmapped.fq
read1sai=CHC7B.unmapped.sai
bam=CHC7B.unmapped.bam
sam=CHC7B.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/1-mapping

bwa aln -I \
                /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
                        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
                                >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
-r "@RG\tID:m7b\tSM:m7b\tLB:m7b\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM

