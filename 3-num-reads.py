D = {}
inFile = open('/netshare1/home1/people/hansun/Data/HeLa/Illumina/ERR0498-04-05.mpileup')
line = inFile.readline()
line = inFile.readline()
line = inFile.readline()
for line in inFile:
    fds = line.split('\t')
    k = fds[0] + ':' + fds[1]
    if line[0:5] == 'INDEL':
        fs = fds[7].split('=')[3].split(',')[0:4]
    else:
        fs = fds[7].split('=')[2].split(',')[0:4]
    ref = int(fs[0]) + int(fs[1])
    alt = int(fs[2]) + int(fs[3])
    D[k] = alt

def dep(SNV):
    n = 0.0
    for k in SNV:
        if k in D:
            n += D[k]
        else:
            n += 0
    return n/len(D)


inFile.close()
inFile = open('Identified-Peptides-Corresponding-Reads')
ouFile = open('Identified-Peptides-Corresponding-Reads2', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[0]
    #if line.find('SNV')!=-1 and line.find('SV')!=-1:
    if line.find('SNV:') != -1:
        R = {}
        fds = line.split('SNV:')
        for x in fds:
            if x[0:3] == 'chr':
                k = ':'.join(x.split(':')[0:2])
                R[k] = 1
    d = int(dep(R))
    ouFile.write(pep + '\t' + str(d) + '\n')
        

    elif line.find('INDEL:') != -1:
        pass
    else:
        R = {}
        fds = line.split(':')
        for item in fds:
            if item.find('ERR') == 0:
                R[item] = 1
        ouFile.write(pep + '\t' + str(len(R)) + '\n')
        



inFile.close()
ouFile.close()
