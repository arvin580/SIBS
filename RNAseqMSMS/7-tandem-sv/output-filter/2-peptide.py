def pep(inF):
    inFile = open(inF)
    
    D = {}
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        start = int(fields[4].split(':')[0])
        pre = fields[4].split(':')[5]
        post = fields[4].split(':')[6]
        #s = int(fields[1].split(':')[-3])
        #e = int(fields[1].split(':')[-2])
        D.setdefault(fields[3], [])
        #D[fields[3]].append(fields[1]+':'+str(s-start+1)+':'+str(e-start+1)+':'+pre+':'+post)
        D[fields[3]].append(fields[0].strip()+':'+fields[1]+':'+str(-1)+':'+str(-1)+':'+pre+':'+post)
    
    inFile.close()
    
    ouFile = open(inF+'-pep','w')
    for k in D:
        v = '\t'.join(D[k])
        ouFile.write(k+'\t'+v+'\n')
    
    ouFile.close()

pep('HeLa-SV-Deletion')
pep('HeLa-SV-Duplication')
pep('HeLa-SV-Inversion')
pep('HeLa-SV-Translocation')
pep('HeLa-Predict-Splicing')
pep('HeLa-Predict')
