import os
os.chdir('genome')

#types=[exonic;splicing, upstream;downstream, downstream, splicing, UTR5, ncRNA_exonic, intergenic, ncRNA_UTR5, intronic, ncRNA_UTR3, exonic, ncRNA_splicing, UTR3, upstream, UTR5;UTR3, ncRNA_UTR5;ncRNA_UTR3, ncRNA_intronic]


types=['exonic','exonic;splicing','splicing','intronic','UTR5','UTR3','UTR5;UTR3','upstream','downstream','upstream;downstream','ncRNA_exonic','ncRNA_splicing','ncRNA_intronic','ncRNA_UTR5','ncRNA_UTR3','ncRNA_UTR5;ncRNA_UTR3','intergenic']


dict1=dict()
dict2=dict()

inFile=open('sum_snp.genome_combined.sorted.pass012.known')
ouFile=open('sum_snp.genome_combined.sorted.pass012.known.stat','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    type=fields[0]
#    dict1.setdefault(type,[0]*24)

#    for i,item in enumerate(fields[-20:]) :
#        if int(item)>0 :
#            dict1[type][i+4]+=1
#    if sum([int(i) for i in fields[-20:-10]])>0 :
#        dict1[type][2]+=1
#    if sum([int(i) for i in fields[-10:]])>0 :
#        dict1[type][3]+=1
#    if sum([int(i) for i in fields[-20:]])>0 :
#        dict1[type][1]+=1
#    if sum([int(i) for i in fields[-20:-10]])>0 and  sum([int(i) for i in fields[-10:]])>0 :
#        dict1[type][0]+=1

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

for key in dict1 :
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

ouFile.close()
