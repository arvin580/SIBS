cd /fs01/szzhongxin/proj1/hansun/12sViruses/5-split
db=/fs01/szzhongxin/proj1/hansun/12sViruses/5-split/human.viruses.target.fa

query=ICC8A.unmapped.sam.unmapped.fa.fa
out=${query}.blasted

blat $db $query  -out=blast8 $out

