D = {}

def unique(inF,flag=''):
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip('>\n')
        line2 = inFile.readline().strip()
        if line1:
            D.setdefault(line2,[])
            line1 = ':'.join(line1.split('\t'))
            if flag:
                D[line2].append(flag+':'+line1)
            else:
                D[line2].append(line1)
        else:
            break
    inFile.close()

unique('Homo_sapiens.GRCh37.70.pep.all.fa.fa')
unique('ERR0498-04-05.unmapped.unique.human-viruse.pep-KR','HUMAN-VIRUS')
unique('unmapped-blated-viruses-90-60.seq.pep-KR','VIRUS')

ouFile = open('Homo_known-protein_virus-KR.fasta','w')
for k in D:
    ouFile.write('>'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')
    #ouFile.write('>REVERSE:'+'|'.join(D[k])+'\n')
    #ouFile.write(k[::-1]+'\n')

ouFile.close()

