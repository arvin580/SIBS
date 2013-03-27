inFile = open('ha')
for line in inFile:
    line = line.strip()
    if line[-1]!='K' and line[-1]!='R':
        print(line)
inFile.close()
