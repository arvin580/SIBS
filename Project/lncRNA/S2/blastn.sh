cd /netshare1/home1/people/hansun/Project/lncRNA/S2
db=/netshare1/home1/people/hansun/Project/lncRNA/S2/GenomeSeq/Human/ucsc.hg19.fasta
#query=xist.human.fa
#out=xist.human.out

query=xist.mouse.fa
out=xist.mouse.out

blastn  -db $db  -query $query -out $out -outfmt 6 -num_threads 6 
