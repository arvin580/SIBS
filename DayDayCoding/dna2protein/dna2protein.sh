## human
#cd /netshare1/home1/people/hansun/DayDayCoding/dna2protein/human
#python  ../App1_RefGene.py  ucsc.hg19.fasta.fa hg19_refGene.txt >dna_protein_out1 2>dna_protein_out2
#python ../cmp_dna_protein1.py protein_human.txt  dna_protein_out1
#python ../cmp_dna_protein2.py protein_human.txt  dna_protein_out1
#python ../cmp_dna_protein3.py   dna_protein_out1.anno dna_protein_score_all dna_protein_score_notfind_all
#python  ../cmp_dna_protein4.py dna_protein_score_all

## mouse
#cd /netshare1/home1/people/hansun/DayDayCoding/dna2protein/mouse
#python  ../App1_RefGene.py  mm9.fasta.fa mm9_refGene.txt >mm9_dna_protein_out1 2>mm9_dna_protein_out2
#python ../cmp_dna_protein1.py protein_mouse.txt  mm9_dna_protein_out1
#python ../cmp_dna_protein2.py protein_mouse.txt mm9_dna_protein_out1 
#python ../cmp_dna_protein3.py   mm9_dna_protein_out1.anno mm9_dna_protein_score_all mm9_dna_protein_score_notfind_all


## rat
#cd /netshare1/home1/people/hansun/DayDayCoding/dna2protein/rat
#python  ../App1_RefGene.py  rn4.fasta.fa rn4_refGene.txt >rn4_dna_protein_out1 2>rn4_dna_protein_out2
#python ../cmp_dna_protein2.py protein_rat.txt rn4_dna_protein_out1
#python ../cmp_dna_protein3.py   rn4_dna_protein_out1.anno rn4_dna_protein_score_all rn4_dna_protein_score_notfind_all

## c.elegans
#cd /netshare1/home1/people/hansun/DayDayCoding/dna2protein/c.elegans
#python  ../App1_RefGene.py  ce10.fasta.fa ce10_refGene.txt >ce10_dna_protein_out1 2>ce10_dna_protein_out2
#python ../cmp_dna_protein2.py protein_c.elegans.txt  ce10_dna_protein_out1
#python ../cmp_dna_protein3.py  ce10_dna_protein_out1.anno ce10_dna_protein_score_all ce10_dna_protein_score_notfind_all


## d.melanogaster
cd /netshare1/home1/people/hansun/DayDayCoding/dna2protein/d.melanogaster
python  ../App1_RefGene.py  dm3.fasta.fa dm3_refGene.txt >dm3_dna_protein_out1 2>dm3_dna_protein_out2
python ../cmp_dna_protein1.py protein_d.melanogaster.txt  dm3_dna_protein_out1
python ../cmp_dna_protein2.py protein_d.melanogaster.txt   dm3_dna_protein_out1
python ../cmp_dna_protein3.py  dm3_dna_protein_out1.anno dm3_dna_protein_score_all dm3_dna_protein_score_notfind_all












