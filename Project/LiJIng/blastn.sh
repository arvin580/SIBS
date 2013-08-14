cd /netshare1/home1/people/hansun/Project/LiJIng
db=uniprot_sprot.2012.11.23.fasta
query=PDB.fasta
out=PDB-blasted.fasta
blastp  -db $db  -query $query -out $out -outfmt 6  
