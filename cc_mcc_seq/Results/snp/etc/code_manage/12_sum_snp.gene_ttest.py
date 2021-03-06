import os

os.chdir('exome')

dict1=dict()
inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1.setdefault(fields[1],[0]*21)
    
    for i,item in enumerate(fields[-20:]) :
        dict1[fields[1]][1+i]+=int(item)
        dict1[fields[1]][0]+=int(item)


inFile.close()

d=dict1.items()
d.sort(cmp=lambda x,y:cmp(x[1][0],y[1][0]),reverse=True) 




ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.gene_ttest','w')
for item in d :
    ouFile.write(item[0]+'\t')
    ouFile.write('\t'.join([str(i) for i in item[1]])+'\n')
ouFile.close()

