D = {}
inFile = open('HeLa-Human-Viruses-pep')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]]=1
inFile.close()
inFile = open('HeLa-Known-Protein-pep')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]]=1
inFile.close()
inFile = open('HeLa-Viruses-pep')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]]=1
inFile.close()

inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-random-10000-seq')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-random-10000-seq-msms','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    n = 0
    for item in fields:
        fds = item.split(':')
        flag = 0
        for fd in fds[1:]:
            for k in D:
                if k in fd:
                    flag += 1
        if flag:
            n += 1
    ouFile.write(str(n)+'\n')

inFile.close()
ouFile.close()







