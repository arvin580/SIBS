#cd /netshare1/home1/people/hansun/Data/S3/blast

#db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta
#query=lncdb.human.fa
#out=lncdb.human.out1
#blastn  -db $db  -query $query -out $out -outfmt 6    -num_threads 6
#####################################################################

cd /netshare1/home1/people/hansun/Project/FLNA 
humandb=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta
mousedb=/netshare1/home1/people/hansun/Data/GenomeSeq/Mouse/ucsc.mouse.fasta
ratdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Rat/ucsc.rat.fasta
chickendb=/netshare1/home1/people/hansun/Data/GenomeSeq/Chicken/ucsc.chicken.fasta
chimpanzeedb=/netshare1/home1/people/hansun/Data/GenomeSeq/Chimpanzee/ucsc.chimpanzee.fasta
cowdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Cow/ucsc.cow.fasta
dogdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Dog/ucsc.dog.fasta
elephantdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Elephant/ucsc.elephant.fasta
fugudb=/netshare1/home1/people/hansun/Data/GenomeSeq/Fugu/ucsc.fugu.fasta
opossumdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Opossum/ucsc.opossum.fasta
platypusdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Platypus/ucsc.platypus.fasta
tetraodondb=/netshare1/home1/people/hansun/Data/GenomeSeq/Tetraodon/ucsc.tetraodon.fasta
xenopusdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Xenopus/ucsc.xenopus.fasta
zebrafishdb=/netshare1/home1/people/hansun/Data/GenomeSeq/Zebrafish/ucsc.zebrafish.fasta



query=flna.fa
out=$query.human.blasted
blastn  -db $humandb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.mouse.blasted
blastn  -db $mousedb  -query $query -out $out -outfmt 6   


query=flna.fa
out=$query.rat.blasted
blastn  -db $ratdb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.chicken.blasted
blastn  -db $chickendb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.chimpanzee.blasted
blastn  -db $chimpanzeedb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.cow.blasted
blastn  -db $cowdb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.dog.blasted
blastn  -db $dogdb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.elephant.blasted
blastn  -db $elephantdb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.fugu.blasted
blastn  -db $fugudb  -query $query -out $out -outfmt 6   


query=flna.fa
out=$query.opossum.blasted
blastn  -db $opossumdb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.platypus.blasted
blastn  -db $platypusdb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.tetraodon.blasted
blastn  -db $tetraodondb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.xenopus.blasted
blastn  -db $xenopusdb  -query $query -out $out -outfmt 6   

query=flna.fa
out=$query.zebrafish.blasted
blastn  -db $zebrafishdb  -query $query -out $out -outfmt 6   














