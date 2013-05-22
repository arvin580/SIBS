import string

def seq(ch,start,end):
    trans = string.maketrans('ATCGatcg','TAGCtagc')
    if ch[0:2] == 'ch':
        inFile = open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            if line1:
                if line1 == '>'+ch:
                    if start <= end:
                        seq = line2[start-1:end].upper()
                    else:
                        seq = string.translate(line2[end-1:start][::-1],trans).upper()
                    return seq
            else:
                break
        inFile.close()
    elif ch[0:2] == 'NC':
        inFile = open('/netshare1/home1/people/hansun/Data/VirusesGenome/VirusesGenome.fasta.fa')
        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            if line1:
                if line1.find('>'+ch) == 0:
                    if start <= end:
                        seq = line2[start-1:end].upper()
                    else:
                        seq = string.translate(line2[end-1:start][::-1],trans).upper()
                    return seq
            else:
                break
        inFile.close()


def td(L):
    LR = []
    for item in L:
        if item == '0':
            LR.append('<td></td>')
        else:
            LR.append('<td>%s</td>'%item)
    return '\n'.join(LR)
        

def diagram(inF):
    '''
    inFile = open(inF)
    L0 = ['0']*76
    L1 = ['0']*76
    L2 = ['0']*76
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            for i in range(len(line2)):
                L0[i] = line2[i]

            ch1 = fields[3]
            start1 = int(fields[10])
            end1 = int(fields[11])
            start1_query = int(fields[8])
            end1_query = int(fields[9])
            ch2 = fields[15]
            start2 = int(fields[22])
            end2 = int(fields[23])
            start2_query= int(fields[20])
            end2_query=int(fields[21])
    
            seq1 = seq(ch1,start1, end1)
            seq2 = seq(ch2,start2, end2)
            for i in range(start1_query-1, end1_query):
                L1[i]=seq1[i-start1_query+1]

            for i in range(start2_query-1, end2_query):
                L2[i]=seq2[i-start2_query+1]

        else:
            break
    inFile.close()
    '''
    L1 = ['A','T','C','G','0','0']
    #print(''.join(L1))
    #print(''.join(L0))
    #print(''.join(L2))
    print(td(L1))
diagram('ha')
