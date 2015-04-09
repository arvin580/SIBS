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


inFile2=open('1.sv.stat')
ouFile=open('1.sv.stat'+'.gene','w')

for line in inFile2 :
    line = line.strip()
    fields=line.split('\t')
    ouFile.write(fields[0]+'\t')
    for item in fields[1:]:
        ch=item.split(':')[0]
        start=item.split(':')[1]
        end=item.split(':')[2]
        gene = []

        for it in genes :
        #if head[0] == item[2]  and head[2]==item[3]:
            if ch == it[2]  :
                if int(it[4])<=int(start)<=int(it[5]) or int(it[4])<=int(end)<=int(it[5]) or (int(start)<=int(it[4]) and int(end)>=int(it[5])):
                    gene.append(it[-1])
        if gene:
            g = item+':'+'/'.join(uniqueList(gene))
        else:
            g = item
        ouFile.write(g+'\t')
    ouFile.write('\n')

inFile2.close()
ouFile.close()

