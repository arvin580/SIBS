def codon():
    D = {}
    inFile = open('CodonUsage')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[0]] = fields[1]
    inFile.close()
    return D

def translate(seq,frame=''):
    seq = seq.upper()
    D = codon()
    P = []
    if frame == 0:
        for i in range(0,len(seq),3):
            #P.append(D[seq[i:i+3]])
            print(D[seq[i:i+3]])
    if frame == 1:
        pass
    if frame == 2:
        pass
    if frame == -1:
        pass
    if frame == -2:
        pass
    if frame == -3:
        pass
    if frame == '':
        pass

translate('ATCGGATCGCTGGAT',0)
