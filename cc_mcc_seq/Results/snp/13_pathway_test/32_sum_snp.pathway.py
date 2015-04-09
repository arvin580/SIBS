import re

dict1=dict()
inFile=open('/netshare1/home1/people/hansun/Data/KEGG/kegg_gene_symbol2')

for line in inFile :
    line=line.strip()
    fields=re.split(r'[\t:]',line)
    dict1[fields[0]]=fields[1:]

inFile.close()


dict2=dict()
dict3=dict()

ouFile1=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.gene_ttest.pathway1','w')
ouFile2=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.gene_ttest.pathway2','w')

for key in dict1 :
    dict2.setdefault(key,[0]*21)
    dict3.setdefault(key,[])
    inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.gene_ttest')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        if fields[0] in dict1[key] :
            for i in range(20) :
                dict2[key][i+1]+=int(fields[i+2])
                dict2[key][0]+=int(fields[i+2])
            dict3[key].append(fields)
    inFile.close()

for key in dict2 :
    if dict2[key][0]>0 :
        ouFile1.write(key+'\t'+'\t'.join([str(i) for i in dict2[key]])+'\n')


for key in dict3 :
    if len(dict3[key])>0 :
        for item in dict3[key] :
            ouFile2.write(key+'\t'+'\t'.join(item)+'\n')


 



ouFile1.close()
ouFile2.close()







