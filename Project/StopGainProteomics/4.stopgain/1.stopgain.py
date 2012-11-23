A = ['C','E','G','K','L','Q','S','R','W','Y']
L = 6
inFile = open('human_uniprot_sprot.digested.fa')
ouFile = open('human_uniprot_sprot.digested.stopgain.fa', 'w')
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        if len(seq) >= L:
            hds = head.split(':')
            ouFile.write(hds[0]+ ':' +hds[1]+':'+hds[2]+':'+'Uniprot'+':'+':'.join(hds[3:]) + '\n')
            ouFile.write(seq + '\n')
            for a in A:
                if a in seq:
                    if seq.index(a)>=L:
                        hds = head.split(':')
                        ouFile.write(hds[0]+ ':' +hds[1]+':'+str(int(hds[1])+seq.index(a)-1)+':'+'StopGain'+':'+':'.join(hds[3:]) + '\n')
                        ouFile.write(seq[0:seq.index(a)] + '\n')
    else:
        break
inFile.close()
ouFile.close()
