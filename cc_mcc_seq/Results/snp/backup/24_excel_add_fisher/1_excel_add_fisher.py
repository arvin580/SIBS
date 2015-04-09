inFile=open('sum_snp.exome_combined.sorted.pass012.new_cc_num_len2_fisher')

dict1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=fields[1]

inFile.close()


inFile=open('sum_snp.exome_combined.sorted.pass012.new_cc_num_len2_fisher.fdr')

dict2=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict2[fields[0]]=fields[1]

inFile.close()



inFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc_num_len2_fisher')

dict3=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict3[fields[0]]=fields[1]

inFile.close()

inFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc_num_len2_fisher.fdr')

dict4=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict4[fields[0]]=fields[1]

inFile.close()


inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus.fisher','w')

for line in inFile :
    fields=line.split('\t')

    if fields[10] in dict1 :
        ouFile.write(dict1[fields[10]]+'\t')
    else :
        ouFile.write('-1'+'\t')

    if fields[10] in dict2 :
        ouFile.write(dict2[fields[10]]+'\t')
    else :
        ouFile.write('-1'+'\t')
 
    if fields[10] in dict3 :
        ouFile.write(dict3[fields[10]]+'\t')
    else :
        ouFile.write('-1'+'\t')
 
    if fields[10] in dict4 :
        ouFile.write(dict4[fields[10]]+'\t')
    else :
        ouFile.write('-1'+'\t')
    
    ouFile.write(line)


inFile.close()
