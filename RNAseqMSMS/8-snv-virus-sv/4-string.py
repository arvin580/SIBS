D = {}
inFile = open('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation')
ouFile = open('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation-string','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]]=1
inFile.close()

STRING = {}
inFile = open('/netshare1/home1/people/hansun/Data/String/protein.links.v9.05.human.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    STRING.setdefault(fields[0],[])
    for item in fields:
        if item in D:
            STRING[fields[0]].append('('+item+')')
        else:
            STRING[fields[0]].append(item)

inFile.close()
for k in STRING:
    ouFile.write('\t'.join(STRING[k])+'\n')

ouFile.close()
