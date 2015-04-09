import re
inFile=open('/netshare1/home1/people/hansun/Data/Cosmic/cancer_gene_census.tsv')
dict1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1.setdefault(fields[0],['1'])
    dict1[fields[0]].append(fields[7])
    dict1[fields[0]].append(fields[8])
    s=re.search(r'lung|hepatocellular|hcc|cholangiocarcinoma',line,re.I)
    if s :
        dict1[fields[0]][0]='2'
inFile.close()

#for key in dict1 :
#    print(key+'\t'+'\t'.join(dict1[key]))

inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus','w')

for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    if fields[9] in dict1 :
        ouFile.write(dict1[fields[9]][0]+'\t'+line+'\n')
    else :
        ouFile.write(''+'\t'+line+'\n')

inFile.close()
ouFile.close()
