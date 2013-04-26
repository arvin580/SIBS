D = {}
inFile = open('genage_human.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[1],0)
    D[fields[1]]+=1
inFile.close()

print(D)
