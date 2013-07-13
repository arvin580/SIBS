D = {}
def normal(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for i in range(len(fields)):
            if fields[i].find('Velos1_NaNa')!=-1:
                f = fields[i]
                no = fields[i+27]
                fno = f + ':' + no
                D.setdefault(fno,0)
                D[fno] += 1
    inFile.close()

normal('HeLa-known-GluC-evidence-unique')
for k in D:
    print(k+'\t'+str(D[k])+'\n')
    
