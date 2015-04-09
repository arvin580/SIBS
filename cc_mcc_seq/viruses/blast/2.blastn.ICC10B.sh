cd /netshare1/home1/szzhongxin/proj1/hansun/viruses/blast
db=/netshare1/home1/szzhongxin/proj1/hansun/Viruses/bwa/hg19.viruses.fasta

query=ICC10B.unmapped.sam.mapped.fa.fa
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  
