cd /netshare1/home1/szzhongxin/proj1/hansun/viruses/splited
db=/netshare1/home1/szzhongxin/proj1/hansun/Viruses/bwa/hg19.viruses.fasta

query=CHC6B.unmapped.sam.unmapped.fa.fa.blasted.split.m1.fa
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  
