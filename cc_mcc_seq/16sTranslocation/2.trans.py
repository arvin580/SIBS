import sys
D = {}
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.trans', 'w')

if sys.argv[1].find('ICC4A') == -1:
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        k = ':'.join(fields[0].split(':')[0:7])
        D.setdefault(k,[])
        D[k].append(line)
    inFile.close()
    for k in D:
        if len(D[k])==2:
            if D[k][0].split('\t')[2]!=D[k][1].split('\t')[2]:
                if sys.argv[1].find('B') != -1:
                    fields = D[k][0].split('\t')
                    seq1 = fields[0]+':1'+'\t'+'\t'.join(fields[1:])
                    fields = D[k][1].split('\t')
                    seq2 = fields[0]+':2'+'\t'+'\t'.join(fields[1:])
                    ouFile.write(seq1+'\n')
                    ouFile.write(seq2+'\n')
     
                else:
                    ouFile.write(D[k][0]+'\n')
                    ouFile.write(D[k][1]+'\n')
    ouFile.close()
else:
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0].find(':')!=-1:
            k = ':'.join(fields[0].split(':')[0:7])
        elif fields[0].find('_')!=-1:
            k = '_'.join(fields[0].split('_')[0:7])
        D.setdefault(k,[])
        D[k].append(line)
    inFile.close()
    for k in D:
        if len(D[k])==2:
            if D[k][0].split('\t')[2]!=D[k][1].split('\t')[2]:
                ouFile.write(D[k][0]+'\n')
                ouFile.write(D[k][1]+'\n')
    ouFile.close()

    
