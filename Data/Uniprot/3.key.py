inFile = open('human_uniprot_sprot.fa')
D = {}
while True:
    head = inFile.readline()
    seq = inFile.readline()
    if head:
        D[head]=1
    else:
        break
inFile.close()
print(len(D))
