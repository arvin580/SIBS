cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/3-unmapped-mouse
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Mouse/ucsc.mouse.fasta
query=ERR0498-04-05.unmapped.unique.163.fasta.blated.unmapped
out=${query}.blated
blat $db $query  -out=blast8 $out
