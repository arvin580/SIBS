###  python ctx_gene.py  /netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/1A/1A.bam.predSV.txt.ctx

import sys

def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist


genes=[]
inFile1=open('/netshare1/home1/people/hansun/Data/hg19_refGene/hg19_refGene.txt','r')

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
    inFile=open(inF)
    ouFile=open(inF+'.gene','w')
    
    while True:
        line1 = inFile.readline().strip()
        if line1:
            fields=line1.split('\t')
            ch1 = fields[0].split(':')[0]
            point1 = fields[0].split(':')[1]
            ch2 = fields[0].split(':')[2]
            point2 = fields[0].split(':')[3]

            gene = []
            for it in genes :
            #if head[0] == item[2]  and head[2]==item[3]:
                if (ch1 == it[2] and int(it[4])<=int(point1)<=int(it[5]))  or (ch2 == it[2] and int(it[4])<=int(point2)<=int(it[5])) :
                    gene.append(it[-1])
            ouFile.write('|'.join(uniqueList(gene))+'\t'+line1+'\n')
        else:
            break
    
    
    inFile.close()
    ouFile.close()



sv('split-mapped-deletion.normal.seq.filtered2.num')
