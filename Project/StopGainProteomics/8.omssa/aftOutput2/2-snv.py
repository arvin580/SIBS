import string

def read_seq():
    pass

D = read_seq()

def diff(codon):
    CODON=['TAA','TAG','TGA']
    SNV = []
    for c in CODON:
        n = 0
        p = 0
        for i in range(len(c)):
            if c[i]==codon[i].upper():
                n += 1
            else:
                p = i
        if n == 2:
            SNV.append([codon,c,p,codon[p],c[p]])
    return SNV

x=diff('CGA')
print(x)


'''    
def seq(ch,pos,strand):
    s = []
    if strand=='+':
        codon= D[ch][pos:pos+3]
        df = diff(codon)
        if df:
            s = [ch,pos+df[2],df[3],df[4]]
    elif strand=='-':
        trans= string.maketrans('atcgATCG','tagcTAGC')
        codon = D[ch][pos:pos+3]
        codon = string.translate(condon[::-1],trans)
        df = diff(codon)
        if df:
            s = [ch,pos+2-df[2],string.translate(df[3]),string.translate(df[4])]
    return s


def snv(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[]
        strand = fields[]
        start = int(fields[])
        end = int(fields[])
        if strand == '+':
            pos = end
            seq(ch,pos,strand)
        elif strand == '-':
            pos = end - 4
            seq(ch,pos,strand)
    inFile.close()
'''
