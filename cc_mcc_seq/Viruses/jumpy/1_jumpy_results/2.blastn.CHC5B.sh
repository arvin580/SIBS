cd /netshare1/home1/szzhongxin/proj1/hansun/Viruses/jumpy/1_jumpy_results
db=/netshare1/home1/szzhongxin/proj1/hansun/Viruses/bwa/hg19.viruses.fasta

query=CHC5B.jmp.br.fasta
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  
