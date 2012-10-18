#cd /netshare1/home1/people/hansun/Project/lncRNA/S3/blast

#db=/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/Human/ucsc.hg19.fasta
#query=ucsc.human.fa
#out=ucsc.human.out1
#blastn  -db $db  -query $query -out $out -outfmt 6  -num_threads 8  -num_threads 6
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



cd /netshare1/home1/people/hansun/Project/lncRNA/S3/blast5
query=lncrna_ucsc_human_genomic.fa



out=ucsc.human.human.out
blastn  -db $humandb  -query $query -out $out -outfmt 6  -num_threads 8 

out=ucsc.human.mouse.out
blastn  -db $mousedb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.rat.out
blastn  -db $ratdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.chicken.out
blastn  -db $chickendb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.chimpanzee.out
blastn  -db $chimpanzeedb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.cow.out
blastn  -db $cowdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.dog.out
blastn  -db $dogdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.elephant.out
blastn  -db $elephantdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.fugu.out
blastn  -db $fugudb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.opossum.out
blastn  -db $opossumdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.platypus.out
blastn  -db $platypusdb  -query $query -out $out -outfmt 6  -num_threads 8  


out=ucsc.human.tetraodon.out
blastn  -db $tetraodondb  -query $query -out $out -outfmt 6  -num_threads 8  


out=ucsc.human.xenopus.out
blastn  -db $xenopusdb  -query $query -out $out -outfmt 6  -num_threads 8  

out=ucsc.human.zebrafish.out
blastn  -db $zebrafishdb  -query $query -out $out -outfmt 6  -num_threads 8  
