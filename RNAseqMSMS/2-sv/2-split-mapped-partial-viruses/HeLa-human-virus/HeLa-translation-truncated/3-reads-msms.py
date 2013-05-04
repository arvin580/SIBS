ouFile = open('HeLa-msms-identified-reads','w')
D2 = {}
inFile = open('HeLa-Known-Protein')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields:
        its = item.split(':')
        for it in its:
            if it[0:3]=='ERR' and it.find('.')!=-1:
                D2.setdefault(it,[])
                D2[it].append(line)
inFile.close()

inFile = open('HeLa-Human-Viruses')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields:
        its = item.split(':')
        for it in its:
            if it[0:3]=='ERR' and it.find('.')!=-1:
                D2.setdefault(it,[])
                D2[it].append(line)
inFile.close()

inFile = open('HeLa-Viruses')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields:
        its = item.split(':')
        for it in its:
            if it[0:3]=='ERR' and it.find('.')!=-1:
                D2.setdefault(it,[])
                D2[it].append(line)
inFile.close()



for k in D2:
    ouFile.write(k+'\t'+'|'.join(D2[k])+'\n')

ouFile.close()

