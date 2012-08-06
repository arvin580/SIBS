import os
import re

def get_pos(pep) :
    D='FDR'
    files=os.listdir(D)
    for f in files :
        inFile=open(D+os.path.sep+f)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            if len(fields)>9 :
                if fields[9]==pep :
                    start=int(fields[5])
                    end=int(fields[6])
                    tmp=fields[2].split('+')[0].split('|')
                    pre=int(tmp[-2])
                    post=int(tmp[-1])
                    return([pre,post,start,end])

        inFile.close()



def make_pos(inF):
    
    inFile=open(inF)
    ouFile=open(inF+'.pos','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        pep=fields[0]
        num=int(fields[1])
        pos=get_pos(pep)
        ouFile.write(pep+'\t'+str(num)+'\t'+str(pos[0])+'\t'+str(pos[1])+'\t'+str(pos[2])+'\t'+str(pos[3])+'\n')
    inFile.close()
    ouFile.close()

make_pos('FDR.pep.genefusions.final')
make_pos('FDR.pep.splicing.final')
