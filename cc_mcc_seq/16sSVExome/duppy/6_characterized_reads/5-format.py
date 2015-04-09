import re
def reads(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        if line.find('>')==0:
            head = line.lstrip('>')
            D.setdefault(head,[])
        else:
            D[head].append(line)
    inFile.close()

    D2 = {}
    for k in D:
        flag = 0
        for item in D[k]:
            s = re.split(r'\s+',item)
            if len(s)>=2:
                if len(s[0])>30 and len(s[-1])>30:
                    D2[k]= ''.join(s)
                    flag = 1
                    break
        if flag == 0:
            print('warning: '+ k)

    ouFile = open(inF+'.formated', 'w')
    d = D2.items()
    d.sort(cmp = lambda x,y :cmp(x[0],y[0]))
    for item in d:
        ouFile.write(item[0]+ '\t' +item[1]+ '\n')
    ouFile.close()
            
reads('16s-exome.duplication.exon.reads')
reads('16s-exome.duplication.gene.reads')

