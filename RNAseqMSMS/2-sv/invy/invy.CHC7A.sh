cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/invy


hg19=/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta

sample=/netshare1/home1/people/hansun/Data/Lundberg/Illumina/ERR0498-04-05.bam

SampleID=ERR0498-04-05

invy -z . -p -g $hg19 -i ${SampleID} -b ${SampleID}.inv.br.txt -o ${SampleID}.inv.txt -r ${SampleID}.inv_merge.txt -k ${SampleID}.inv.br_merge.txt $sample 
