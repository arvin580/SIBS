dict1=dict()
inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1.setdefault(fields[1],0)
    
    for item in fields[-20:] :
        dict1[fields[1]]+=int(item)

inFile.close()

d=dict1.items()
d.sort(cmp=lambda x,y:cmp(x[1],y[1]),reverse=True) 




ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted','w')
for item in d :
    inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        if fields[1]==item[0] :
            ouFile.write(line+'\n')
    
    inFile.close()

ouFile.close()

