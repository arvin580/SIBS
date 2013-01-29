cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/ERR0498-04-05-fasta
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta
query=ERR0498-04-05.unmapped.unique.32.fasta
out=${query}.blasted
blastn  -db $db  -query $query -out $out -outfmt 6
