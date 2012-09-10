inFile=open('hg19_refGene.txt')
ouFile=open('hg19_refGene_exon_max_len','w')
dict1=dict()

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    start=fields[9]
    end=fields[10]
    symbol=fields[12]
    dict1.setdefault(symbol,[])
    starts=start.split(',')
    ends=end.split(',')
    length=0
    lh=0
    for i in range(len(starts)-1) :
        lh=int(ends[i])-int(starts[i])
        length+=lh
    dict1[symbol].append(length)


inFile.close()


for key in dict1 :
    ouFile.write(key+'\t'+str(max(dict1[key]))+'\n')
