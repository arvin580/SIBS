from RefGene_class import *

a=RefGene()
a.calculate_Coding_NoCoding_Intronic_Intergenic_Length()

#inFile=open('hg19_refGene.txt')

#refGene=RefGene()
#for line in inFile :
#    refGene.read_one_gene(line)
#    refGene.calculate_Coding_NoCoding_Intronic_Intergenic_Length()
#inFile.close()
#print('Coding')
#print(len(refGene.CodingDict))
#print('NonCoding')
#print(len(refGene.NonCodingDict))
#print('Intronic')
#print(len(refGene.IntronicDict))
#print('NonIntergenic')
#print(len(refGene.NonIntergenicDict))
#print('NRNM')
#print(refGene.NRNM)
'''
chrom=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
'chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20',
'chr21','chr22','chrX','chrY']
inFile=open('hg19.chr.len')
G1=0
G2=0
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[0] in chrom :
        G1+=int(fields[1])
    G2+=int(fields[1])

inFile.close()
print('Genome chr1 chr2  Length')
print(G1)
print('Genome chrxxx Length')
print(G2)
'''
