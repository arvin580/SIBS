import os
os.chdir('genome')


ouFile=open('sum_snp.genome_combined.sorted.pass012.new.type3','w')
inFile=open('sum_snp.genome_combined.sorted.pass012.new')

dict1=dict()

for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')

    type=fields[0]
    dict1.setdefault(type,[0]*23)

    for i,item in enumerate(fields[-20:]) :
        if int(item)>0 :
            dict1[type][i+3]+=1
    if sum([int(i) for i in fields[-20:-10]])>0 :
        dict1[type][1]+=1
    if sum([int(i) for i in fields[-10:]])>0 :
        dict1[type][2]+=1
    if sum([int(i) for i in fields[-20:]])>0 :
        dict1[type][0]+=1


inFile.close()

type=['exonic','exonic;splicing','splicing','intronic','UTR5','UTR3','UTR5;UTR3','ncRNA_exonic','ncRNA_splicing','ncRNA_intronic','ncRNA_UTR5','ncRNA_UTR3','ncRNA_UTR5;ncRNA_UTR3','upstream','downstream','upstream;downstream','intergenic']

for key in type :
    #ouFile.write(key+'\t'+str(dict1[key])+'\n')
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

ouFile.close()


'''
exonic	7891
exonic;splicing	134
splicing	110


intronic	252859

UTR5	1497
UTR3	5954
UTR5;UTR3	2

ncRNA_exonic	1344
ncRNA_splicing	7
ncRNA_intronic	15922
ncRNA_UTR5	23
ncRNA_UTR3	112
ncRNA_UTR5;ncRNA_UTR3	1

upstream	4562
downstream	4361
upstream;downstream	212

intergenic	387390

'''
