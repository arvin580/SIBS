cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/4-sv-blast
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta
query=test.fa
out=${query}.blated
#blat $db $query  -out=blast8 $out
blastn  -db $db  -query $query -out $out 
