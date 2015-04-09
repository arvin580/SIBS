def delly():
    inFile = open('br.txt')
    sv = {}
    seq = []
    for line in inFile:
        le = line
        line = line.strip()
        fields = line.split()
        if len(fields) > 2:
            if fields[0].find('chr')!=0:
                seq.append(le)
            else:
                k=':'.join(fields)
                sv[k] = seq 
                seq = []
    inFile.close()
    return sv



def count(inF):
    D = dict()
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D.setdefault(fields[0],0)
        D[fields[0]]+=1
    inFile.close()

    d = D.items()
    d.sort(cmp=lambda x,y:cmp(x[1],y[1]))

    sv = delly()
    for item in d:
        if item[1]<3:
            #for x in sv[item[0]]:
            #    print(x)
            print(item[0])

count('delly.br.filtered.blasted')
    
    
