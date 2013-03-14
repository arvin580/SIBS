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
        line2 = inFile.readline().strip()
        if line1:
            fields=line1.split('\t')
            ch = fields[3]
            start = fields[10]
            end = fields[11]
            gene = []
            for it in genes :
            #if head[0] == item[2]  and head[2]==item[3]:
                if ch == it[2]  :
                    if int(it[4])<=int(start)<=int(it[5]) or int(it[4])<=int(end)<=int(it[5]) or (int(start)<=int(it[4]) and int(end)>=int(it[5])):
                        gene.append(it[-1])
            if gene:
                g = ch+':'+str(start)+':'+str(end)+':'+':'+'/'.join(uniqueList(gene))
            else:
                g = ch+':'+str(start)+':'+str(end)
            ouFile.write(g+'\n')

            ch = fields[15]
            start = fields[22]
            end = fields[23]
            gene = []
            for it in genes :
            #if head[0] == item[2]  and head[2]==item[3]:
                if ch == it[2]  :
                    if int(it[4])<=int(start)<=int(it[5]) or int(it[4])<=int(end)<=int(it[5]) or (int(start)<=int(it[4]) and int(end)>=int(it[5])):
                        gene.append(it[-1])
            if gene:
                g = ch+':'+str(start)+':'+str(end)+':'+'/'.join(uniqueList(gene))
            else:
                g = ch+':'+str(start)+':'+str(end)
            ouFile.write(g+'\n')

        else:
            break
    
    
    inFile.close()
    ouFile.close()



#sv('split-mapped-deletion')
#sv('split-mapped-inversion')
sv('split-mapped-duplication')
#sv('split-mapped-translocation')
