import re

def conservation(inF,consD) :
    inFile=open(inF)
    for line in inFile :
        line=line.strip()
        if line.find('fixedStep')==0 :
            s=re.search(r'start=(\d+)',line)
            if s :
                start=int(s.group(1))
                offset=0
        else :
            consD[start+offset]=float(line)
            offset+=1
    inFile.close()

consD=dict()
conservation('chr1.phastCons46way.wigFix',consD)
