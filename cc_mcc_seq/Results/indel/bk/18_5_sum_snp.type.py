import os
os.chdir('genome')



dict1=dict()
dict1['genomic']=309.56939830
dict1['exonic']=6.38689240
dict1['intronic']=91.78244030
dict1['UTR']=15.59631540
dict1['ncRNA']=12.29157400
dict1['intergenic']=188.90479750

dict2=dict()
dict2['genomic']=38125.6
dict2['exonic']=422.1
dict2['intronic']=13744.5
dict2['UTR']=411.1
dict2['ncRNA']=958.3
dict2['intergenic']=22080.1

dict3=dict()
dict3['genomic']=42556.5
dict3['exonic']=443.0
dict3['intronic']=15006.1
dict3['UTR']=447.2
dict3['ncRNA']=1107.5
dict3['intergenic']=24962.1

type=['genomic','exonic','intronic','UTR','ncRNA','intergenic']


ouFile=open('sum_snp.genome_combined.sorted.pass012.new.type.stat.fisher','w')
from scipy import stats
for i,item1 in enumerate(type[0:-1]) :
    for item2 in type[i+1:] :
        pvalue=stats.fisher_exact([[dict2[item1],dict2[item2]],[dict1[item1],dict1[item2]]])[1]
        ouFile.write('CC\tGenome\t'+item1+'\t'+item2+'\t'+str(pvalue)+'\n')

        pvalue=stats.fisher_exact([[dict3[item1],dict3[item2]],[dict1[item1],dict1[item2]]])[1]
        ouFile.write('MCC\tGenome\t'+item1+'\t'+item2+'\t'+str(pvalue)+'\n')

        pvalue=stats.fisher_exact([[dict2[item1],dict2[item2]],[dict3[item1],dict3[item2]]])[1]
        ouFile.write('CC\tMCC\t'+item1+'\t'+item2+'\t'+str(pvalue)+'\n')


ouFile.close()



