def pep(inF):
    inFile = open(inF)
    
    D = {}
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        start = int(fields[4].split(':')[0])
        end = int(fields[4].split(':')[1])
        e = fields[4].split(':')[2]
        hyper = fields[4].split(':')[3]
        pre = fields[4].split(':')[5]
        post = fields[4].split(':')[6]
        miss = fields[4].split(':')[7]
        modi = []
        try:
            modi = fields[5].split(':')
            for i in range(1,len(modi),3):
                modi[i] = str(int(modi[i]) - start + 1)
        except:
            pass
        modi = ':'.join(modi)
        #s = int(fields[1].split(':')[-3])
        #e = int(fields[1].split(':')[-2])
        D.setdefault(fields[3], [])
        #D[fields[3]].append(fields[1]+':'+str(s-start+1)+':'+str(e-start+1)+':'+pre+':'+post)
        D[fields[3]].append(fields[0].strip()+'|'+fields[1]+'|'+e+'|'+hyper+'|'+miss+'|'+pre+'|'+post+'|'+modi)
    
    inFile.close()
    
    ouFile = open(inF+'-pep','w')
    for k in D:
        v = '\t'.join(D[k])
        ouFile.write(k+'\t'+v+'\n')
    
    ouFile.close()

pep('HeLa-Viruses')
pep('HeLa-Human-Viruses')
pep('HeLa-Known-Protein')
