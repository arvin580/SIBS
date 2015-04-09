inFile1=open('snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV','r')
dict1=dict()
for line in inFile1 :
    fields=line.split('\t')
    gene=fields[2].split(':')[0]
    dict1.setdefault(gene,[0]*20)
    for i,item in enumerate(fields[17:]) :
        it=item.split(':')[0]
        if it=='0/1' or it=='1/0' or it=='1/1' :
            dict1[gene][i]+=1

inFile1.close()

inFile1=open('snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV','r')
for line in inFile1 :
    fields=line.split('\t')
    gene=fields[2].split(':')[0]
    dict1.setdefault(gene,[0]*20)
    for i,item in enumerate(fields[17:]) :
        it=item.split(':')[0]
        if it=='0/1' or it=='1/0' or it=='1/1' :
            dict1[gene][i+10]+=1

inFile1.close()

ouFile1=open('snpindel12_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV.geneLevel.distribution','w')

for item in sorted(dict1.items(),key=lambda x:sum(x[1]),reverse=True) :
    ouFile1.write(item[0]+'\t'+'\t'.join([str(x) for x in item[1]])+'\n')
ouFile1.close()
