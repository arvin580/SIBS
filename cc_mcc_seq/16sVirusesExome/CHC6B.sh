cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome
samtools view /netshare1/home1/szzhongxin/proj1/hansun/mapping8/6B/6B.bam |python 1.filter.py >CHC6B.unmapped
python 2.fq.py CHC6B.unmapped

read1fq=CHC6B.unmapped.fq
read1sai=CHC6B.unmapped.sai
bam=CHC6B.unmapped.bam
sam=CHC6B.unmapped.sam

cd /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/1-mapping

bwa aln -I \
                /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
                        /netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
                                >$read1sai

bwa samse  \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/bwa/viruses \
$read1sai \
/netshare1/home1/szzhongxin/proj1/hansun/16sVirusesExome/$read1fq \
-r "@RG\tID:m6b\tSM:m6b\tLB:m6b\tPL:illumina\tPU:barcode" >$sam
#samtools view -bS -o $bam -

#samtools  sort $bam $bamsorted

#mv $bamsortedbam $BAM
#samtools index $BAM

