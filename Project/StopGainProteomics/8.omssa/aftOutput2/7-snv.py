import string

def read_seq():
    inFile = open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
    D = {}
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            D[line1.strip('>')]=line2
        else:
            break
    inFile.close()
    return D

D = read_seq()
print(len(D))

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



def seq(ch,pos,strand):
    s = []
    if strand=='+':
        codon= D[ch][pos:pos+3]
        df = diff(codon)
        if df:
            s = [ch,pos+df[0][2],df[0][3],df[0][4],df[0][0],df[0][1]]
    elif strand=='-':
        trans= string.maketrans('atcgATCG','tagcTAGC')
        codon = D[ch][pos:pos+3]
        codon = string.translate(condon[::-1],trans)
        df = diff(codon)
        if df:
            s = [ch,pos+2-df[0][2],string.translate(df[0][3]),string.translate(df[0][4]),df[0][0],df[0][1]]
    return s


def snv(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[1]
        start = int(fields[8])
        end = int(fields[9])
        if start <= end:
            strand = '+'
        else:
            strand = '-'
        if strand == '+':
            pos = end
            s = seq(ch,pos,strand)
        elif strand == '-':
            pos = end - 4
            s = seq(ch,pos,strand)
        print(line)
        print(s)
    inFile.close()

snv('3-stopgain-protein-unique2-filtered.blated.filtered.part')
