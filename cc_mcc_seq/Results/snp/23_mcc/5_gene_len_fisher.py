total_mutation=381256
total_length=3137161264
from scipy import stats

inFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc_num_len2')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc_num_len2_fisher','w')
ouFile2=open('sum_snp.exome_combined.sorted.pass012.new_mcc_num_len2_fisher2','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if int(fields[2])<10000 :
        fisher=stats.fisher_exact([[int(fields[1]),int(fields[2])],[total_mutation,total_length]])
        ouFile.write(fields[0]+'\t'+str(fisher[1])+'\n')
    else :
        ouFile2.write(line+'\n')


inFile.close()
