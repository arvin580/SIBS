import os

def fdr_stat(d) :
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
                dict1.setdefault(cls,[])
                dict1[cls].append(line)
        inFile.close()
    ouFile=open(d+'.spec.stat','w')
    for key in dict1 :
        ouFile.write(key+'\t'+str(len(dict1[key]))+'\n')
    
    ouFile.close()

fdr_stat('FDR')
fdr_stat('FDR_fusions')
fdr_stat('FDR_splicing')
