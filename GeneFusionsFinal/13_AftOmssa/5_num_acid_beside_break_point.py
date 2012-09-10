def num_acid(inF) :
    inFile=open(inF)
    ouFile=open(inF+'.3.3','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
    
        point=int(fields[2])
        start=int(fields[4])
        end=int(fields[5])
        
        bef=point-start+1
        aft=end-point
        #k=str(bef)+':'+str(aft)
        #dict1.setdefault(k,0)
        #dict1[k]+=1
    
        if bef>=3 and aft>=3 :
            ouFile.write(line+'\n')
    
    inFile.close()
    ouFile.close()

num_acid('FDR.pep.genefusions.final.pos')
num_acid('FDR.pep.splicing.final.pos')
