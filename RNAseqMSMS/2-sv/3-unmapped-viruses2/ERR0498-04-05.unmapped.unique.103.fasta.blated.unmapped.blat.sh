cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/3-unmapped-viruses2
db=/fs01/szzhongxin/proj1/hansun/Viruses/bwa/hg19.viruses.fasta
query=ERR0498-04-05.unmapped.unique.103.fasta.blated.unmapped
out=${query}.blated
blat $db $query  -out=blast8 $out
