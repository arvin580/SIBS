def pep(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for i in range(len(fields)):
            if fields[i].find('PREDICT-SPLICING')==0:
                start = int(fields[i+3].split(':')[0])
                end = int(fields[i+3].split(':')[1])
                e = fields[i+3].split(':')[2]
                hyper = fields[i+3].split(':')[3]
                pre = fields[i+3].split(':')[5]
                post = fields[i+3].split(':')[6]
                miss = fields[i+3].split(':')[7]
                modi = []
                try:
                    modi = fields[i+4].split(':')
                    for i in range(1,len(modi),3):
                        modi[i] = str(int(modi[i]) - start + 1)
                except:
                    pass
                modi = ':'.join(modi)
                #s = int(fields[1].split(':')[-3])
                #e = int(fields[1].split(':')[-2])
                D.setdefault(fields[i+2], [])
                #D[fields[3]].append(fields[1]+':'+str(s-start+1)+':'+str(e-start+1)+':'+pre+':'+post)
                D[fields[i+2]].append(fields[0].strip()+'|'+fields[i]+'|'+e+'|'+hyper+'|'+miss+'|'+pre+'|'+post+'|'+modi)
                break
    inFile.close()
    
    ouFile = open(inF+'-pep','w')
    for k in D:
        v = '\t'.join(D[k])
        ouFile.write(k+'\t'+v+'\n')
    
    ouFile.close()

#pep('HeLa-SV-Deletion')
#pep('HeLa-SV-Duplication')
#pep('HeLa-SV-Inversion')
#pep('HeLa-SV-Translocation')
pep('HeLa-Predict-Splicing')
#pep('HeLa-Predict')
