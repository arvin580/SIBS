###  python ctx_gene.py  /netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/1A/1A.bam.predSV.txt.ctx

import sys

def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist


genes=[]
inFile1=open('/netshare1/home1/szzhongxin/proj1/hansun/annotation/annovar/humandb/hg19_refGene.txt','r')

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
    exon_starts = fields[9].split(',')
    exon_ends = fields[10].split(',')
    for i in range(len(exon_starts)-1):
        gene.append([exon_starts[i],exon_ends[i]])
    genes.append(gene)

inFile1.close()


inFile2=open('1.sv.stat')
ouFile=open('1.sv.stat'+'.exon','w')

for line in inFile2 :
    line = line.strip()
    fields=line.split('\t')
    ouFile.write(fields[0]+'\t')
    for item in fields[1:]:
        ch1=item.split(':')[0]
        start=item.split(':')[1]
        ch2=item.split(':')[2]
        end=item.split(':')[3]
        gene1 = []
        gene2 = []

        for it in genes :
        #if head[0] == item[2]  and head[2]==item[3]:
            if ch1 == it[2]  :
                for x in it[7:]:
                    if int(x[0])<=int(start)<=int(x[1]):
                        gene1.append(it[6])
            if ch2 == it[2]  :
                for x in it[7:]:
                    if int(x[0])<=int(end)<=int(x[1]):
                        gene2.append(it[6])
   
        if gene1 and not gene2:
            g = item+':'+'/'.join(uniqueList(gene1))+':'+'*'
        if gene2 and not gene1:
            g = item+':'+'*'+':'+'/'.join(uniqueList(gene2))
        if gene1 and gene2:
            g = item+':'+'/'.join(uniqueList(gene1))+':'+'/'.join(uniqueList(gene2))
        if not gene1 and not gene2:
            g = item
        ouFile.write(g+'\t')
    ouFile.write('\n')

inFile2.close()
ouFile.close()

