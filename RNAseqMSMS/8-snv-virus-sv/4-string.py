D = {}
inFile = open('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation')
ouFile = open('HeLa-Gene-SNV-Virus-Deletion-Duplication-Inversion-Translocation-string','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]]=1
inFile.close()

STRING = {}
STRING2 = {}
inFile = open('/netshare1/home1/people/hansun/Data/String/protein.links.v9.05.human.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    STRING.setdefault(fields[0],[])
    STRING2.setdefault(fields[0],0)
    for item in fields:
        if item in D:
            STRING[fields[0]].append('('+item+')')
            STRING2[fields[0]]+=1

        else:
            STRING[fields[0]].append(item)

inFile.close()
for k in STRING:
    ouFile.write(str(STRING2[k])+'\t'+str(len(STRING[k]))+'\t'+str(float(STRING2[k])/len(STRING[k]))+'\t'+'\t'.join(STRING[k])+'\n')

ouFile.close()
