inFile = open('human_uniprot_sprot.digested.fa')
ouFile = open('human_uniprot_sprot.digested.6acid.fa','w')

while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        if len(seq) >=6 :
            ouFile.write(':'.join(head.split(':')[0:3])+'\n')
            ouFile.write(seq+'\n')
    else:
        break


inFile.close()
ouFile.close()

