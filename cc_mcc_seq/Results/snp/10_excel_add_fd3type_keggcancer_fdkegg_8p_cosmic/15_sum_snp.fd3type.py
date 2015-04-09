dict1=dict()
dict2=dict()
dict3=dict()

inFile=open('/netshare1/home1/szzhongxin/proj1/hansun/Results/fudanhelp/gene_symbol_inflammation_found')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    for item in fields :
        dict1.setdefault(item,[])
        dict1[item].append(line)

inFile.close()

inFile=open('/netshare1/home1/szzhongxin/proj1/hansun/Results/fudanhelp/gene_symbol_metastasis_found')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    for item in fields :
        dict2.setdefault(item,[])
        dict2[item].append(line)


inFile.close()

inFile=open('/netshare1/home1/szzhongxin/proj1/hansun/Results/fudanhelp/gene_symbol_stemcell_found')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    for item in fields :
        dict3.setdefault(item,[])
        dict3[item].append(line)




inFile.close()



inFile1=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue')
ouFile1=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type','w')

for line in inFile1 :
    type=[]
    line=line.strip()
    fields=line.split('\t')
    if fields[5] in dict3 :
        type.append('stemcell')
    if fields[5] in dict2:
        type.append('metastasis')
    if fields[5] in dict1 :
        type.append('inflammation')

    ouFile1.write(';'.join(type)+'\t'+line+'\n')
inFile1.close()
ouFile1.close()
