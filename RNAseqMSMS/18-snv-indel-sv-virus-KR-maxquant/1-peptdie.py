inFile = open('evidence.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[8].find('known')!=-1:
        pass
    elif fields[8].find('')!=-1:
        pass
inFile.close()
