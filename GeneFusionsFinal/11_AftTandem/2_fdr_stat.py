import os

def fdr_stat(d) :

    dict1=dict()
    dict2=dict()
    dict3=dict()
    dict4=dict()

    D=d
    dict1=dict()
    files=os.listdir(D)
    for fi in files :
        inFile=open(D+'/'+fi)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            if len(fields)>2:
                cls=fields[2].split(':')[0]
                pep=fields[9]
                #dict1.setdefault(cls,[])
                #dict1[cls].append(line)
                if cls=='genefusions' :
                    dict1.setdefault(pep,0)
                    dict1[pep]+=1
                if cls=='splicing' :
                    dict2.setdefault(pep,0)
                    dict2[pep]+=1
                if cls=='annotated' :
                    dict3.setdefault(pep,0)
                    dict3[pep]+=1
                if cls=='contaminated' :
                    dict4.setdefault(pep,0)
                    dict4[pep]+=1
        inFile.close()
    ouFile=open(d+'.pep.stat','w')
    ouFile1=open(d+'.pep.genefusions','w')
    ouFile2=open(d+'.pep.splicing','w')
    ouFile3=open(d+'.pep.annotated','w')
    ouFile4=open(d+'.pep.contaminated','w')

    ouFile.write('genefusions'+'\t'+str(len(dict1))+'\n')
    for key in dict1 :
        ouFile1.write(key+'\t'+str(dict1[key])+'\n')

    ouFile.write('splicing'+'\t'+str(len(dict2))+'\n')
    for key in dict2 :
        ouFile2.write(key+'\t'+str(dict2[key])+'\n')


    ouFile.write('annotated'+'\t'+str(len(dict3))+'\n')
    for key in dict3 :
        ouFile3.write(key+'\t'+str(dict3[key])+'\n')

    ouFile.write('contaminated'+'\t'+str(len(dict4))+'\n')
    for key in dict4 :
        ouFile4.write(key+'\t'+str(dict4[key])+'\n')
  
    ouFile.close()

fdr_stat('FDR')
fdr_stat('FDR_fusions')
fdr_stat('FDR_splicing')
