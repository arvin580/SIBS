dict1=dict()
dict2=dict()
dict3=dict()
dict4=dict()

inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.point_ttest_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=fields[2]


inFile.close()



inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.gene_ttest_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict2[fields[0]]=fields[2]

inFile.close()

inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.point_ranksum_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict3[fields[0]]=fields[2]


inFile.close()




inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.gene_ranksum_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict4[fields[0]]=fields[2]

inFile.close()



inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ouFile.write(dict4[fields[1]]+'\t'+dict3[fields[21]+':'+fields[22]]+'\t'+dict2[fields[1]]+'\t'+dict1[fields[21]+':'+fields[22]]+'\t'+'\t'.join(fields)+'\n')





inFile.close()
ouFile.close()
