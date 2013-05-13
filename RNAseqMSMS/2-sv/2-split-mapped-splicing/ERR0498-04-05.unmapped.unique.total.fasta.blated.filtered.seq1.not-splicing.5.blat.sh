cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/2-split-mapped-splicing
db=/netshare1/home1/people/hansun/Data/ucsc/refMrna-2013-5-13.fasta.fa
query=ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing.5.fa
out=${query}.blated
blat $db $query  -out=blast8 $out
