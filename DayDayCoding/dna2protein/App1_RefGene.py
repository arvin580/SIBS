import sys


fasta=sys.argv[1]
refGene=sys.argv[2]

#fasta='ucsc.hg19.fasta.fa'
#refGene=hg19_refGene.txt

from RefGene_class import *

inFile1=open(fasta)
hg=inFile1.readlines()
inFile1.close()

#ouFile=open('hahaha','w')


inFile=open(refGene)
#inFile=open('hg19_refGene.part.txt')
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
        for i in xrange(len(refGene.coding_position)-3) :
            refGene.point_change(refGene.coding_position[i],refGene.coding_atcg[i],refGene.coding_atcg[i])
            #ouFile.write(''.join(refGene.coding_atcg)+'\n')


inFile.close()
#ouFile.close()


