inFile = open('SRR040290.sam')
ouFile = open('SRR040290.sam.select','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)>10:
        if fields[2]=='chr2':
            if 10263474<=int(fields[3])<=10263721:
                ouFile.write(line+'\n')

inFile.close()
ouFile.close()
