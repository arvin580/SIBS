inFile=open('/netshare1/home1/people/hansun/Data/hg19_refGene/hg19_refGene.txt')

dict1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1.setdefault(fields[1],[])
    dict1[fields[1]].append(fields[12])
inFile.close()

#for key in dict1 :
#    print(key+'\t'+'\t'.join(dict1[key]))
#    if len(set(dict1[key])) >1 :
#        print(key)


def nm2sym(file) :
    inFile=open(file)
    ouFile=open(file+'.sym','w')
    
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        if fields[4] in dict1 :
            ouFile.write(dict1[fields[4]][0]+'\t'+line+'\n')
        else :
            ouFile.write('0'+'\t'+line+'\n')
            print('0'+'\t'+line)

    inFile.close()
    ouFile.close()

nm2sym('diff_RNA_isoform_CCC_AvsB.txt')
nm2sym('diff_RNA_isoform_MCC_AvsB.txt')
nm2sym('diff_RNA_isoform_CCCCvsMCC.txt')

