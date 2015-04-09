inFile=open('sum_snp.exome_combined.sorted.pass012.new.gene_ttest_2group_mcc_sorted')
dict1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if int(fields[3])>0 :
        dict1[fields[0]]=1
inFile.close()

inFile=open('sum_snp.exome_combined.sorted.pass012.new.gene_ttest_2group_cc_sorted')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.gene_ttest_2group_cc_mcc_intersection','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if int(fields[2])>0 :
        if fields[0] in dict1 :
            ouFile.write(line+'\n')
inFile.close()
ouFile.close()
