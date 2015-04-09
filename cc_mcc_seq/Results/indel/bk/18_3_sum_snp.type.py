import os
os.chdir('genome')



ouFile=open('sum_snp.genome_combined.sorted.pass012.known.type2','w')
inFile=open('sum_snp.genome_combined.sorted.pass012.known')

dict2=dict()
dict2['exonic']=[0]*20
dict2['intronic']=[0]*20
dict2['UTR']=[0]*20
dict2['updownstream']=[0]*20
#dict2['ncRNA_exonic']=[0]*20
#dict2['ncRNA_intronic']=[0]*20
#dict2['ncRNA_UTR']=[0]*20
dict2['ncRNA']=[0]*20
dict2['intergenic']=[0]*20
dict2['genomic']=[0]*20

type=['exonic','exonic;splicing','splicing','intronic','UTR5','UTR3','UTR5;UTR3','ncRNA_exonic','ncRNA_splicing','ncRNA_intronic','ncRNA_UTR5','ncRNA_UTR3','ncRNA_UTR5;ncRNA_UTR3','upstream','downstream','upstream;downstream','intergenic']
#type2=['exonic','intronic','UTR','updownstream','ncRNA','intergenic']
type2=['genomic','exonic','intronic','UTR','ncRNA','intergenic']

dict1=dict()

for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    dict1.setdefault(fields[0],[0]*20)
    for i,item in enumerate(fields[-20:]) :
        dict1[fields[0]][i]+=int(item)
inFile.close()


for key in dict1 :

    for i in range(20) :
        dict2['genomic'][i]+=dict1[key][i]

    if key in type[0:3] :
        for i in range(20) :
            dict2['exonic'][i]+=dict1[key][i]
    if key in type[3:4] :
        for i in range(20) :
            dict2['intronic'][i]+=dict1[key][i]
    if key in type[4:7] :
        for i in range(20) :
            dict2['UTR'][i]+=dict1[key][i]
    if key in type[7:13] :
        for i in range(20) :
            dict2['ncRNA'][i]+=dict1[key][i]
    if key in type[13:16] :
        for i in range(20) :
            dict2['updownstream'][i]+=dict1[key][i]
    if key in type[16:] :
        for i in range(20) :
            dict2['intergenic'][i]+=dict1[key][i]


for key in type2 :
    #ouFile.write(key+'\t'+str(dict1[key])+'\n')
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict2[key]])+'\n')

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
