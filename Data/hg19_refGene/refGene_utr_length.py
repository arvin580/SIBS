inFile=open('hg19_refGene.txt')
ouFile=open('hg19_refGene_utr_max_len','w')
dict1=dict()

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    start1=int(fields[4])
    end1=int(fields[5])
    start2=int(fields[6])
    end2=int(fields[7])
    symbol=fields[12]
    dict1.setdefault(symbol,[])
    length=start2-start1+end1-end2
    dict1[symbol].append(length)

inFile.close()


for key in dict1 :
    ouFile.write(key+'\t'+str(max(dict1[key]))+'\n')
