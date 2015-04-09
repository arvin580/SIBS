from scipy import stats
import numpy as np

list1=list()

inFile=open('sum_snp.exome_combined.sorted.pass012.new.point_ttest')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.point_ranksum_out','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    tt=stats.ranksums([int(i) for i in fields[2:12]],[int(j) for j in fields[12:22]])
    oneline=fields[0:2]+[str(tt[1])]+fields[2:]
    list1.append(oneline)

inFile.close()

list1.sort(cmp=lambda x,y :cmp(float(x[2]),float(y[2])))

for item in list1 :
    ouFile.write('\t'.join(item)+'\n')



