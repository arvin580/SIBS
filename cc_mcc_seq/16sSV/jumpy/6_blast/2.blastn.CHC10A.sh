cd /netshare1/home1/szzhongxin/proj1/hansun/16sSV/jumpy/6_blast
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta

query=CHC10A.jmp.sam.unique.paired.fa
out=${query}.blated

#blastn  -db $db  -query $query -out $out -outfmt 6  -max_target_seqs 20    
blat $db $query  -out=blast8 $out
