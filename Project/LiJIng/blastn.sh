cd /netshare1/home1/people/hansun/Project/LiJIng
db=human_uniprot_sprot.fa
query=PDB.fasta.fa
out=PDB-blasted
blastp  -db $db  -query $query -out $out -outfmt 6  
