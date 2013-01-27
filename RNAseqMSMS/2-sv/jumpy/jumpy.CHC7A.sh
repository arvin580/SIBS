cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/jumpy


hg19=/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta

sample=/netshare1/home1/people/hansun/Data/Lundberg/Illumina/ERR0498-04-05.bam

SampleID=ERR0498-04-05

jumpy -z . -p -g $hg19 -i ${SampleID} -b ${SampleID}.jmp.br.txt -o ${SampleID}.jmp.txt -r ${SampleID}.jmp_merge.txt -k ${SampleID}.jmp.br_merge.txt $sample
