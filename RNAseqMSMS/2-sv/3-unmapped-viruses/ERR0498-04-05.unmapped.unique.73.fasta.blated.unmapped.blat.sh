cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/3-unmapped-viruses
db=/netshare1/home1/people/hansun/Data/VirusesGenome/VirusesGenome.fasta
query=ERR0498-04-05.unmapped.unique.73.fasta.blated.unmapped
out=${query}.blated
blat $db $query  -out=blast8 $out
