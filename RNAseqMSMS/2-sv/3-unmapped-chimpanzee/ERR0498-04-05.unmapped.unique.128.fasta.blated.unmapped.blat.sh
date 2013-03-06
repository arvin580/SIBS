cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/3-unmapped-chimpanzee
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Chimpanzee/ucsc.chimpanzee.fasta
query=ERR0498-04-05.unmapped.unique.128.fasta.blated.unmapped
out=${query}.blated
blat $db $query  -out=blast8 $out
