cd /netshare1/home1/szzhongxin/proj1/hansun/viruses/split
db=/netshare1/home1/szzhongxin/proj1/hansun/viruses/split/human.viruses.target.fa

query=CHC7B.unmapped.sam.unmapped.fa.fa
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  
