cd /netshare1/home1/szzhongxin/proj1/hansun/16sSV/jumpy/4_blast
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta

query=tmp.CHC10A.jmp.fa
out=tmp.${query}.blasted

#blastn -db $db  -query $query -out $out -outfmt 6  -max_target_seqs 1
/netshare1/home1/people/hansun/MySoft/blast/ncbi-blast-2.2.27+/bin/blastn -db $db  -query $query -out $out -outfmt 6  -num_alignments 2
