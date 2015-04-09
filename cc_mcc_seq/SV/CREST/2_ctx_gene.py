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
    genes.append(gene)

inFile1.close()


inFile2=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.genelevel','w')

for line in inFile2 :
    fields=line.split('\t')
    head=[]
    tail=[]
    head.append(fields[0])
    head.append(fields[1])
    head.append(fields[2])
    head.append([])
    tail.append(fields[4])
    tail.append(fields[5])
    tail.append(fields[6])
    tail.append([])
    for item in genes :
        if head[0] == item[2]  and head[2]==item[3]:
            if int(item[4])<=int(head[1])<=int(item[5]) :
                head[3].append(item[6])
            #else :
            #    head[3].append(head[0]+':'+head[2]+':'+head[1])
        if tail[0] == item[2] and head[2]==item[3]:
            if int(item[4])<=int(tail[1])<=int(item[5]) :
                tail[3].append(item[6])
            #else :
            #    tail[3].append(head[0]+':'+head[2]+':'+head[1])

    ouFile1.write('\t'.join(head[0:3])+'\t'+':'.join(uniqueList(head[3]))+'\t'+'\t'.join(tail[0:3])+'\t'+':'.join(uniqueList(tail[3]))+'\n') 

inFile2.close()
ouFile1.close()

