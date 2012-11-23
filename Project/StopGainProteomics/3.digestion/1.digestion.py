inFile = open('human_uniprot_sprot.fa')
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        index = [0]
        for i in range(len(seq)-1):
            if (seq[i] == 'K' and seq[i+1]!='P') or (seq[i] == 'R' and seq[i+1]!='P'): 
                end = i 
                print(seq[start:end+1])
                start = end + 1
        print(seq[start:len(seq)])
    else:
        break
inFile.close()
