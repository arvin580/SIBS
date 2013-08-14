cd /netshare1/home1/people/hansun/tmp

db=protein.fasta
query=peptide.fasta
out=peptide_protein.blasted

blastp  -db $db  -query $query -out $out -outfmt 6  



