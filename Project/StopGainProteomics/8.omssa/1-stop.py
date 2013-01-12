import sys
D = {}
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.stop','w')
for line in inFile:
    fields = line.split(',')
    pep = fields[2]
    if pep[-1]=='K' or pep[-1]=='R' or pep==' Peptide':
        pass
    else:
        D.setdefault(fields[2], 0)
        D[fields[2]]+=1
inFile.close()

for k in D:
    ouFile.write(k+'\t'+str(D[k])+'\n')



