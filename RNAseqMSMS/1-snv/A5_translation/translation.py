import string

def codon():
    D = {}
    inFile = open('CodonUsage')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[0]] = fields[1]
    inFile.close()
    return D

def translate(seq,frame='',point=''):
    seq = seq.upper()
    trans = string.maketrans('ATCGatcg','TAGCtagc')
    seq_r = string.translate(seq[::-1],trans)

    D = codon()
    P = []
    POS = ''
    FROM = ''
    TO = ''


    if frame == 0:
        for i in range(0,len(seq),3):
            if len(seq[i:i+3]) == 3:
                if seq[i:i+3] in D:
                    P.append(D[seq[i:i+3]])
                else:
                    print('0-frame translation error in ' + seq)
                    break
        return([''.join(P),POS,FROM,TO])

    if frame == 1:
        for i in range(1,len(seq),3):
            if len(seq[i:i+3]) == 3:
                if seq[i:i+3] in D:
                    P.append(D[seq[i:i+3]])
                else:
                    print('1-frame translation error in ' + seq)
                    break
        return([''.join(P),POS,FROM,TO])

    if frame == 2:
        for i in range(2,len(seq),3):
            if len(seq[i:i+3]) == 3:
                if seq[i:i+3] in D:
                    P.append(D[seq[i:i+3]])
                else:
                    print('2-frame translation error in ' + seq)
                    break
        return([''.join(P),POS,FROM,TO])

    if frame == -1:
        for i in range(0,len(seq_r),3):
            if len(seq_r[i:i+3]) == 3:
                if seq_r[i:i+3] in D:
                    P.append(D[seq_r[i:i+3]])
                else:
                    print('-1-frame translation error in ' + seq_r)
                    break
        return([''.join(P),POS,FROM,TO])

    if frame == -2:
        for i in range(1,len(seq_r),3):
            if len(seq_r[i:i+3]) == 3:
                if seq_r[i:i+3] in D:
                    P.append(D[seq_r[i:i+3]])
                else:
                    print('-2-frame translation error in ' + seq_r)
                    break
        return([''.join(P),POS,FROM,TO])


    if frame == -3:
        for i in range(2,len(seq_r),3):
            if len(seq_r[i:i+3]) == 3:
                if seq_r[i:i+3] in D:
                    P.append(D[seq_r[i:i+3]])
                else:
                    print('-3-frame translation error in ' + seq_r)
                    break
        return([''.join(P),POS,FROM,TO])

P=translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',0)
print(P)
P=translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',1)
print(P)
P=translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',2)
print(P)
P=translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',-1)
print(P)
P=translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',-2)
print(P)
P=translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',-3)
print(P)
