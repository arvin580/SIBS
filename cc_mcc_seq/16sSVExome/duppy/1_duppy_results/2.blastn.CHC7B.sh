cd /netshare1/home1/szzhongxin/proj1/hansun/16sSVExome/duppy/1_duppy_results
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta

query=CHC7B.br.fasta
out=${query}.blasted

blastn  -db $db  -query $query -out $out -outfmt 6  -max_target_seqs 20
