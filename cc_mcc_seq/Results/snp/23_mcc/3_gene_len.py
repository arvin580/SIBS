import re
inFile=open('/netshare1/home1/people/hansun/Data/hg19_refGene/hg19_refGene_coding_max_len')

dict1=dict()

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=int(fields[1])

inFile.close()


dict2=dict()
inFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc_num_len2','w')
#ouFile2=open('sum_snp.exome_combined.sorted.pass012.new_cc_num_len_fisher','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    fd=re.split(r'[;,(]',fields[1])[0]
    dict2.setdefault(fields[1],[0,dict1[fd]])
    #dict2[fields[1]][0]+=1
    for item in fields[-10:] :
        dict2[fields[1]][0]+=int(item)


inFile.close()

#from scipy import stats
for key in dict2 :
    ouFile.write(key+'\t'+str(dict2[key][0])+'\t'+str(dict2[key][1])+'\n')

    #fisher=stats.fisher_exact([[dict2[key][0],dict2[key][1]],[329633,3000000000]])
    #ouFile2.write(key+'\t'+str(dict2[key][0])+'\t'+str(dict2[key][1])+'\t'+str(fisher[1])+'\n')

ouFile.close()
#ouFile2.close()



