cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/delly


hg19=/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta

sample=/netshare1/home1/people/hansun/Data/Lundberg/Illumina/ERR0498-04-05.bam

SampleID=ERR0498-04-05

delly -z . -p -d -g $hg19 -i ${SampleID} -b ${SampleID}.br.txt -o ${SampleID}.del.txt  $sample 
