#cd /netshare1/home1/people/hansun/Project/lncRNA/S3/blast

#db=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Human/ucsc.hg19.fasta
#query=xist.mouse.fa
#out=xist.mouse.out1
#blastn  -db $db  -query $query -out $out -outfmt 6  -num_threads 6
#####################################################################

humandb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Human/ucsc.hg19.fasta
mousedb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Mouse/ucsc.mouse.fasta
ratdb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Rat/ucsc.rat.fasta
chickendb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Chicken/ucsc.chicken.fasta
chimpanzeedb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Chimpanzee/ucsc.chimpanzee.fasta
cowdb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Cow/ucsc.cow.fasta
dogdb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Dog/ucsc.dog.fasta
elephantdb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Elephant/ucsc.elephant.fasta
fugudb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Fugu/ucsc.fugu.fasta
opossumdb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Opossum/ucsc.opossum.fasta
platypusdb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Platypus/ucsc.platypus.fasta
tetraodondb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Tetraodon/ucsc.tetraodon.fasta
xenopusdb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Xenopus/ucsc.xenopus.fasta
zebrafishdb=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Zebrafish/ucsc.zebrafish.fasta



cd /netshare1/home1/people/hansun/Project/lncRNA/S3/blast2
query=xist.mouse.fa



out=xist.mouse.human.out
blastn  -db $humandb  -query $query -out $out -outfmt 6 

out=xist.mouse.mouse.out
blastn  -db $mousedb  -query $query -out $out -outfmt 6  

out=xist.mouse.rat.out
blastn  -db $ratdb  -query $query -out $out -outfmt 6  

out=xist.mouse.chicken.out
blastn  -db $chickendb  -query $query -out $out -outfmt 6  

out=xist.mouse.chimpanzee.out
blastn  -db $chimpanzeedb  -query $query -out $out -outfmt 6  

out=xist.mouse.cow.out
blastn  -db $cowdb  -query $query -out $out -outfmt 6  

out=xist.mouse.dog.out
blastn  -db $dogdb  -query $query -out $out -outfmt 6  

out=xist.mouse.elephant.out
blastn  -db $elephantdb  -query $query -out $out -outfmt 6  

out=xist.mouse.fugu.out
blastn  -db $fugudb  -query $query -out $out -outfmt 6  

out=xist.mouse.opossum.out
blastn  -db $opossumdb  -query $query -out $out -outfmt 6  

out=xist.mouse.platypus.out
blastn  -db $platypusdb  -query $query -out $out -outfmt 6  


out=xist.mouse.tetraodon.out
blastn  -db $tetraodondb  -query $query -out $out -outfmt 6  


out=xist.mouse.xenopus.out
blastn  -db $xenopusdb  -query $query -out $out -outfmt 6  

out=xist.mouse.zebrafish.out
blastn  -db $zebrafishdb  -query $query -out $out -outfmt 6  
