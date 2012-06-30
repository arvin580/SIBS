from RefGene_class import *

inFile1=open('ucsc.hg19.fasta.fa')
hg=inFile1.readlines()
inFile1.close()


inFile=open('hg19_refGene.txt')
for line in inFile :
    refGene=RefGene()
    refGene.read_one_gene(line)
    refGene.gene_to_coding()
#refGene.print_coding_position()
#refGene.print_coding_position()
    refGene.check_warning()

    #while True :
    #    line=inFile1.readline().strip()
    #    if line=='>'+refGene.chrom :
    #        chrom=inFile1.readline().strip()
    #        break
    #    if not line :
    #        break

    ch='>'+refGene.chrom+'\n'
    if ch in hg :
        chrom=hg[hg.index(ch)+1]


    if len(refGene.coding_position) >0 :
        #refGene.point_position(refGene.coding_position[0])
        refGene.position_to_atcg(chrom)
        refGene.point_change(refGene.coding_position[0],refGene.coding_atcg[0],refGene.coding_atcg[0])


inFile.close()


