inFile = open('uniprot_sprot.2012.11.23.fa')
ouFile = open('human_uniprot_sprot.fa', 'w')
while True:
    head = inFile.readline()
    seq = inFile.readline()
    if head:
        if head.find('Homo sapiens')!=-1 or head.find('human')!=-1 :
            ouFile.write(head)
            ouFile.write(seq)

    else:
        break
inFile.close()
ouFile.close()
