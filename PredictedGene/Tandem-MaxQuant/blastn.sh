cd  /netshare1/home1/people/hansun/PredictedGene/Tandem-MaxQuant
db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta
query=HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss-Validation.fa
out=HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss-Validation.out2
#tblastn  -db $db  -query $query -out $out -outfmt 6  
tblastn  -db $db  -query $query -out $out 
