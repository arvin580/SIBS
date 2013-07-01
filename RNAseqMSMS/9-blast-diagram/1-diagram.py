import string

def seq2(ch,start,end):
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
D = {}
def read_genome(L):
    for item in L:
        inFile = open(item)
        while True:
            line1 = inFile.readline().strip('>\n')
            line2 = inFile.readline().strip()
            if line1:
                D[line1.split()[0]]=line2
            else:
                break
        inFile.close()

read_genome(['/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa',
'/netshare1/home1/people/hansun/Data/VirusesGenome/VirusesGenome.fasta.fa'])
def seq(ch,start,end):
    trans = string.maketrans('ATCGatcg','TAGCtagc')
    if start <= end:
        seq = D[ch][start-1:end].upper()
    else:
        seq = string.translate(D[ch][end-1:start][::-1],trans).upper()
    return seq


def td(L):
    LR = []
    for item in L:
        if item == '0':
            LR.append('<td></td>')
        else:
            LR.append('<td>%s</td>'%item)
    return '\n'.join(LR)

def td2(L0,L1,L2):
    LR = []
    for i in range(len(L0)):
        if L1[i] == L2[i]:
            LR.append('<td bgcolor="gray">%s</td>'%L0[i])
        elif L1[i]!='0' and L2[i]!='0':
            LR.append('<td bgcolor="orange">%s</td>'%L0[i])
        else:
            LR.append('<td>%s</td>'%L0[i])
    return '\n'.join(LR)
        
def table(ouFile,L0,L1,L2,L0_etc,L1_etc,L2_etc):
    ouFile.write('<table>\n')
    ####caption
    ouFile.write('<caption>\n')
    ouFile.write(L0_etc[0]+'\n')
    ouFile.write('<br />\n')
    ouFile.write('<font color="red">%s:%s-%s</font>\n'%(L1_etc[0],L1_etc[1],L1_etc[2]))
    ouFile.write('<br />\n')
    ouFile.write('<font color="blue">%s:%s-%s</font>\n'%(L2_etc[0],L2_etc[1],L2_etc[2]))
    ouFile.write('</caption>\n')

    ####L1
    ouFile.write('<tr style="color:red">\n')
    ouFile.write(td(L1)+'\n')
    ouFile.write('</tr>\n')
    ####L0
    ouFile.write('<tr>\n')
    ouFile.write(td2(L0,L1,L2)+'\n')
    ouFile.write('</tr>\n')
    ####L2
    ouFile.write('<tr style="color:blue">\n')
    ouFile.write(td(L2)+'\n')
    ouFile.write('</tr>\n')


    ouFile.write('</table>\n')
    ouFile.write('<hr />\n')

def diagram(inF):
    inFile = open(inF)
    ouFile = open(inF+'.html','w')
    ouFile2 = open(inF+'.indel','w')
    ouFile.write('<html>\n')
    ouFile.write('<body>\n')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            L0 = ['0']*76
            L1 = ['0']*76
            L2 = ['0']*76
            L0_etc= []
            L1_etc= []
            L2_etc= []

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

            L0_etc=[fields[0].strip('>')]
            try:
                if start1_query+end1_query<= start2_query+end2_query:
                    for i in range(start1_query-1, end1_query):
                        L1[i]=seq1[i-start1_query+1]
                    for i in range(start2_query-1, end2_query):
                        L2[i]=seq2[i-start2_query+1]
                    L1_etc=[ch1,start1,end1,'gene']
                    L2_etc=[ch2,start2,end2,'gene']
                else:
                    for i in range(start1_query-1, end1_query):
                        L2[i]=seq1[i-start1_query+1]
                    for i in range(start2_query-1, end2_query):
                        L1[i]=seq2[i-start2_query+1]
                    L1_etc=[ch2,start2,end2,'gene']
                    L2_etc=[ch1,start1,end1,'gene']
                table(ouFile,L0,L1,L2,L0_etc,L1_etc,L2_etc)
            except:
                ouFile2.write(line1+'\n')
                ouFile2.write(line2+'\n')
                
        else:
            break
    inFile.close()

    ouFile.write('</body>\n')
    ouFile.write('</html>\n')
    ouFile.close()
    ouFile2.close()
    #L1 = ['A','T','C','G','0','0']
    #print('<table>')
    #print(''.join(L1))
    #print(''.join(L0))
    #print(''.join(L2))
    #print(td(L1))
diagram('ERR0498-04-05.unmapped.unique.human-viruse-checked')
