###  python ctx_gene.py  /netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/1A/1A.bam.predSV.txt.ctx

import sys

def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist

chs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15',
        'chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']


genes=[]
inFile1=open('/netshare1/home1/people/hansun/Data/hg19_refGene/refGene-2013-04-22.txt')

for line in inFile1 :
    fields=line.split('\t')
    gene=[]
    gene.append(fields[0])
    gene.append(fields[1])
    gene.append(fields[2])
    gene.append(fields[3])
    gene.append(fields[4])
    gene.append(fields[5])
    gene.append(fields[12])
    genes.append(gene)

inFile1.close()

def sv(inF):
    D = {}
    inFile=open(inF)
    ouFile1=open(inF+'.gene','w')
    ouFile2=open(inF+'.non-gene','w')
    
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields=line1.split('\t')
            ch1 = fields[3]
            start1 = int(fields[10])
            end1 = int(fields[11])
            start1_query = int(fields[8])
            end1_query = int(fields[9])
            ch2 = fields[15]
            start2 = int(fields[22])
            end2 = int(fields[23])
            start2_query= int(fields[20])
            end2_query=int(fields[21])
            flag = 0
            if ch1 in chs and ch2 in chs:
                for it in genes :
                    if ((ch1 == it[2]) and (int(it[4])<=int(start1)<=int(it[5]) or int(it[4])<=int(end1)<=int(it[5]) or (int(start1)<=int(it[4]) and int(end1)>=int(it[5])) or (int(end1)<=int(it[4]) and int(start1)>=int(it[5])) )) or (ch2 == it[2] and (int(it[4])<=int(start2)<=int(it[5]) or int(it[4])<=int(end2)<=int(it[5]) or (int(start2)<=int(it[4]) and int(end2)>=int(it[5])) or (int(end2)<=int(it[4]) and int(start2)>=int(it[5])) )):
                        gene = it[-1]
                        D.setdefault(gene,[])
                        D[gene].append(line1+'\t'+line2)
                        flag += 1
            if flag == 0:
                ouFile2.write(line1+'\t'+line2+'\n')

        else:
            break
    for k in D: 
        ouFile1.write(k+'\t'+'\t'.join(uniqueList(D[k]))+'\n')
    
    inFile.close()
    ouFile1.close()
    ouFile2.close()



sv('split-mapped-deletion')
#sv('split-mapped-inversion')
#sv('split-mapped-duplication')
#sv('split-mapped-translocation')
