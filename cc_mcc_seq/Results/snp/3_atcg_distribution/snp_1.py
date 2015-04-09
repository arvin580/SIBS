dict1=dict()

atcg=['AT','AC','AG','TA','TC','TG','CA','CT','CG','GA','GT','GC']



ouFile=open('sum_snp.genome_combined.sorted.pass012.new.atcg','w')
inFile=open('sum_snp.genome_combined.sorted.pass012.new')


for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    f1=fields[0]
    f2=fields[24]+fields[25]
    dict1.setdefault(f1,{})
    for item in atcg :
        dict1[f1].setdefault(item,[0]*20)
    for i,item in enumerate(fields[-20:]) :
        if item != '0'  :
            dict1[f1][f2][i]+=1

inFile.close()


def dict2list(d) :
    list1=list()
    for key in atcg :
        #list1.append(key)
        if key in d :
            #list1.append(str(d[key][1]))
            list1=list1+[key]+[str(i) for i in d[key]]
        else :
            list1=list1+[key]+['0']*20
    return list1


for key in dict1 :
        ouFile.write(key+'\t'+'\t'.join(dict2list(dict1[key]))+'\n')

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
