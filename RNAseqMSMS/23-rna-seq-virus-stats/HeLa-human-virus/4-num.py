ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num2','w')

def num(inF,flag):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D.setdefault(int(fields[1]), 0)
        D[int(fields[1])] += 1
    inFile.close()

    d = D.items()
    d.sort(cmp = lambda x,y:cmp(x[0],y[0]))
    ouFile.write(flag+'\t')
    for item in d :
        ouFile.write(str(item[0]) + '\t' + str(item[1])+'\t')
    ouFile.write('\n')

num('ERR0498-04-05.unmapped.unique.human-viruse-checked.num','Virus-Integration')

ouFile.close()
