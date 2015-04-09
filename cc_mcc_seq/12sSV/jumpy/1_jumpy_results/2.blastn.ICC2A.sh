cd /netshare1/home1/szzhongxin/proj1/hansun/12sSV/jumpy/1_jumpy_results
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta

query=ICC2A.jmp.br.fasta
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  -max_target_seqs 20
