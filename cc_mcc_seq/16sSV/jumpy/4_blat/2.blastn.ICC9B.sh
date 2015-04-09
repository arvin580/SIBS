cd /netshare1/home1/szzhongxin/proj1/hansun/16sSV/jumpy/4_blat
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta

query=ICC9B.jmp.fa
out=${query}.blated

blat $db $query  -out=blast8 $out    
