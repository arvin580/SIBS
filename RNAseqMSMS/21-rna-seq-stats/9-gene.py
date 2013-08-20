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

            gene1 = []
            gene2 = []
            for it in genes :
                if (ch1 == it[2] and int(it[4])<=int(point1)<=int(it[5]))   :
                    gene1.append(it[-1])
                if (ch2 == it[2] and int(it[4])<=int(point2)<=int(it[5])) :
                    gene2.append(it[-1])
            if gene1:
                gene1 = '|'.join(uniqueList(gene1))
            else:
                gene1 = '*'
            if gene2:
                gene2 = '|'.join(uniqueList(gene2))
            else:
                gene2 = '*'
            ouFile.write(gene1+':'+gene2+'\t'+line1+'\n')
        else:
            break
    
    
    inFile.close()
    ouFile.close()



sv('split-mapped-translocation.normal.seq.filtered2.num')
