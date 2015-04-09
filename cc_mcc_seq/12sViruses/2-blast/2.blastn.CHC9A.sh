cd /netshare1/home1/szzhongxin/proj1/hansun/12sViruses/2-blast
db=/netshare1/home1/szzhongxin/proj1/hansun/Viruses/bwa/hg19.viruses.fasta

query=CHC9A.unmapped.sam.mapped.fa.fa
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  
