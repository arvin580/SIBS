def protein_anno(dict1) :
    inFile=open('dna_protein_out1.anno')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k=fields[0]+'\t'+fields[1]
        v1=fields[2]+'\t'+fields[3]+'\t'+fields[4]
        if len(fields) >8 :
            #v2='\t'.join(fields[5:])
            v2=fields[7]
        dict1.setdefault(k,[])
        dict1[k].append(v1)
        dict1[k].append(v2)

    inFile.close()
import os
dr='human_score'
def score() :
    dict1=dict()
    protein_anno(dict1)

    ouFile1=open('dna_protein_score_all','w')
    ouFile2=open('dna_protein_score_notfind_all','w')
    for f in os.listdir(dr) :
        if f.find('all.txt')!=-1 : 
            ch=f.split('.')[0]
            inFile=open(dr+'/'+f)
            for line in inFile :
                line=line.strip()
                fields=line.split('\t')
                k=ch+'\t'+fields[0]
                if k in dict1 :
                    ouFile1.write(k+'\t'+fields[1]+'\t'+dict1[k][0]+'\t'+dict1[k][1]+'\n')
                else :
                    ouFile2.write(k+'\t'+fields[1]+'\n')


    inFile.close()
    ouFile1.close()
    ouFile2.close()

score()
