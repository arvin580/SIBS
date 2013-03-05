inFile = open('unmapped.database.fa')
for line in inFile:
    line = line.strip()
    if line.find('sp')!=-1 and line.find('ERR049804')!=-1:
        print(line)
