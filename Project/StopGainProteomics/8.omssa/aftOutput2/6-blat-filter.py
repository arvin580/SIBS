def filter(inF):
    inFile = open(inF)
    ouFile = open(inF+'.filtered', 'w')
    ouFile2 = open(inF+'.filtered2', 'w')
    ouFile3 = open(inF+'.filtered3', 'w')
    D = {}
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[2]=='100.00' and len(fields[0].split(':')[1])==int(fields[3]) \
                and int(fields[4]) == 0 and int(fields[5])==0 :
                    if fields[0] in D:
                        ouFile2.write(line+'\n')
                    else:    
                        ouFile.write(line+'\n')
                        D[fields[0]]=line
        else:
            if fields[0] not in D:
                ouFile3.write(line+'\n')
    inFile.close()
    ouFile.close()

filter('3-stopgain-protein-unique2-filtered.blated')
