import os
os.chdir('genome')

dict1=dict()

dict1['exonic']=[[0],['exonic',0,{}],['exonic;splicing',0,{}],['splicing',0,{}]]
dict1['intronic']=[[0],['intronic',0,{}]]
dict1['UTR']=[[0],['UTR5',0,{}],['UTR3',0,{}],['UTR5;UTR3',0,{}]]
dict1['updownstream']=[[0],['upstream',0,{}],['donwstream',0,{}],['upstream;downstream',0,{}]]
dict1['ncRNA_exonic']=[[0],['ncTNA_exonic',0,{}],['ncRNA_splicing',0,{}]]
dict1['ncRNA_intronic']=[[0],['ncTNA_intronic',0,{}]]
dict1['ncRNA_UTR']=[[0],['ncRNA_UTR5',0,{}],['ncRNA_UTR3',0,{}],['ncRNA_UTR5;ncRNA_UTR3',0,{}]]
dict1['intergenic']=[[0],['intergenic',0,{}]]
type=['exonic','intronic','UTR','updownstream','ncRNA_exonic','ncRNA_intronic','ncRNA_UTR','intergenic']
atcg=['AT','AC','AG','TA','TC','TG','CA','CT','CG','GA','GT','GC']



ouFile=open('sum_snp.genome_combined.sorted.pass012.new.atcg','w')
inFile=open('sum_snp.genome_combined.sorted.pass012.new')


for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    f1=fields[0]
    f2=fields[24]+fields[25]
    f3=sum([int(i) for i in fields[-20:-10]])
    f4=sum([int(i) for i in fields[-10:]])
    for key in dict1 :
        for i,item in enumerate(dict1[key]) :
            if f1 in item :
                dict1[key][0][0]+=1
                dict1[key][i][1]+=1
                dict1[key][i][2].setdefault(f2,[0]*22)
                if f3>0 :
                    dict1[key][i][2][f2][0]+=1
                if f4>0:
                    dict1[key][i][2][f2][1]+=1
                for m,n in enumerate(fields[-20:]):
                    dict1[key][i][2][f2][m+2]+=int(n)


inFile.close()


def dict2list(d) :
    list1=list()
    for key in atcg :
        #list1.append(key)
        if key in d :
            #list1.append(str(d[key][1]))
            list1=list1+[key]+[str(i) for i in d[key]]
        else :
            list1=list1+[key]+['0']*22
    return list1


for key in type :
    for item in dict1[key][1:] :
        ouFile.write(key+'\t'+str(dict1[key][0][0])+'\t'+item[0]+'\t'+str(item[1])+'\t'+'\t'.join(dict2list(item[2]))+'\n')


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
