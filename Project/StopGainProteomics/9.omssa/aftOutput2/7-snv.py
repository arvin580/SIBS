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
            for item in df:
                s.append([ch,pos+item[2],item[3],item[4],'+',item[0],item[1]])
    elif strand=='-':
        trans= string.maketrans('atcgATCG','tagcTAGC')
        codon = D[ch][pos:pos+3]
        codon = string.translate(codon[::-1],trans)
        df = diff(codon)
        if df:
            for item in df:
                s.append([ch,pos+2-item[2],string.translate(item[3],trans),string.translate(item[4],trans),'-',item[0],item[1]])
    return s


def snv(inF):
    inFile = open(inF)
    ouFile = open(inF+'.snv','w')
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
        if s:    
            ouFile.write(line+'\t')
            for item in s:
                ouFile.write('\t'.join([str(x) for x in item])+'\t')
            ouFile.write('\n')
    inFile.close()
    ouFile.close()

snv('3-stopgain-protein-unique2-filtered.blated.filtered')
