dict1=dict()
inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted_mcc_num_len2_fisher.fdr')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted_mcc_num_len2_fisher.fdr.sorted','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=float(fields[1])

inFile.close()

d=dict1.items()
d.sort(cmp=lambda x,y:cmp(x[1],y[1]))

for item in d :
    #ouFile.write(item[0]+'\t'+'%.4f'%(item[1])+'\n')
    ouFile.write(item[0]+'\t'+str(item[1])+'\n')
