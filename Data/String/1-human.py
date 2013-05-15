def human(inF):
    inFile = open(inF)
    ouFile = open(inF.split('.txt')[0]+'.human','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('.')
        if fields[0] == '9606':
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

#human('protein.links.v9.0.txt')


def human2(inF):
    inFile = open(inF)
    ouFile = open(inF.split('.txt')[0]+'.human','w')
    for line in inFile:
        line = line.strip()
        fields = line.split()
        if fields[0] == '9606':
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()



human2('protein.aliases.v9.05.txt')
