cd /netshare1/home1/szzhongxin/proj1/hansun/16sSV/jumpy/4_blast
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta

query=CHC7B.jmp.fa
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  -max_target_seqs 20    
