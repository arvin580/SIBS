cd /netshare1/home1/szzhongxin/proj1/hansun/SV/delly
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta
#query=xist.human.fa
#out=xist.human.out

query=delly.br.filtered.fasta
out=delly.br.filtered.blasted

blastn  -db $db  -query $query -out $out -outfmt 6 -num_threads 6 
