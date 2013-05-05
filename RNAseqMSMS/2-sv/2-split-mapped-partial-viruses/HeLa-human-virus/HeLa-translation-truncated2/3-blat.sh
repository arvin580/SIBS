cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/2-split-mapped-partial-viruses/HeLa-human-virus/HeLa-translation-truncated2
db=/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/HPV-genome.fa
query=ERR0498-04-05.unmapped.unique.human-viruse-checked.fa
out=${query}.blated2
blat -t=dnax -q=prot $db $query  -out=blast8 $out
