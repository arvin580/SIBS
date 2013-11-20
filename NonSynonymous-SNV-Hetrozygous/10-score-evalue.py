def score(inF):
    inFile = open(inF)
    ouFile = open(inF+'-score', 'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            fds = fields[4].split(':')
            ouFile.write(line2 +'\t'+ '\t'.join(fds[2:5])+ '\n')
        else:
            break
    
    inFile.close()
    ouFile.close()

score('Peptides-Identified-First2')
score('Peptides-Identified-Second2')
