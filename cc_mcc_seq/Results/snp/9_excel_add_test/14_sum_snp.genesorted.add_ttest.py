dict1=dict()
dict2=dict()
dict3=dict()
dict4=dict()

inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.point_ttest_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=fields[2]


inFile.close()



inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.gene_ttest_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict2[fields[0]]=fields[2]

inFile.close()

inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.point_ranksum_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict3[fields[0]]=fields[2]


inFile.close()




inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.gene_ranksum_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict4[fields[0]]=fields[2]

inFile.close()



inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ouFile.write(dict4[fields[1]]+'\t'+dict3[fields[21]+':'+fields[22]]+'\t'+dict2[fields[1]]+'\t'+dict1[fields[21]+':'+fields[22]]+'\t'+'\t'.join(fields)+'\n')





inFile.close()
ouFile.close()


dict1=dict()
dict2=dict()
dict3=dict()
dict4=dict()



inFile=open('sum_snp.exome_combined.sorted.pass012.new.point_ttest_out')


for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=fields[2]


inFile.close()



inFile=open('sum_snp.exome_combined.sorted.pass012.new.gene_ttest_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict2[fields[0]]=fields[2]

inFile.close()

inFile=open('sum_snp.exome_combined.sorted.pass012.new.point_ranksum_out')


for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict3[fields[0]]=fields[2]


inFile.close()



inFile=open('sum_snp.exome_combined.sorted.pass012.new.gene_ranksum_out')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict4[fields[0]]=fields[2]

inFile.close()



inFile=open('sum_snp.exome_combined.sorted.pass012.new.genesorted')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.genesorted.tpvalue','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ouFile.write(dict4[fields[1]]+'\t'+dict3[fields[21]+':'+fields[22]]+'\t'+dict2[fields[1]]+'\t'+dict1[fields[21]+':'+fields[22]]+'\t'+'\t'.join(fields)+'\n')





inFile.close()
ouFile.close()
