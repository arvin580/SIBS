import os
import sys

def protein_anno(dict1) :
    inFile=open(sys.argv[1])
    print(sys.argv[1])
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k=fields[0]+'\t'+fields[1]
        v1=fields[2]+'\t'+fields[3]+'\t'+fields[4]
        #v2=''
        if len(fields) >6 :
            #v2='\t'.join(fields[5:])
            #v2=fields[5]
            #v2=fields[6]
            v2=';'.join(fields[x] for x in range(6,len(fields),3))
        if len(fields) ==6 :
            v2=fields[5]
        dict1.setdefault(k,[])
        dict1[k].append(v1)
        dict1[k].append(v2)

    inFile.close()
dr='.'
def score() :
    dict1=dict()
    protein_anno(dict1)

    ouFile1=open(sys.argv[2],'w')
    ouFile2=open(sys.argv[3],'w')
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
                    #ouFile2.write(k+'\t'+fields[1]+'\n')
                    pass


    inFile.close()
    ouFile1.close()
    ouFile2.close()

score()
