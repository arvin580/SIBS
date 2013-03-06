import sys

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.digested', 'w')
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        hs = head.split()
        index = [-1]
        for i in range(len(seq)-1):
            if (seq[i] == 'K' and seq[i+1]!='P') or (seq[i] == 'R' and seq[i+1]!='P'): 
                index.append(i)
        index.append(len(seq)-1)
        for i in range(len(index)-1):
            #hd = hs[0] +':' +str(index[i]+2) +':' +str(index[i+1]+1) +':'+':'.join(hs[1:])
            hd = hs[0] +':' +str(index[i]+2) +':' +str(index[i+1]+1)
            ouFile.write(hd + '\n')
            ouFile.write(seq[index[i]+1:index[i+1]+1] + '\n')
        for i in range(len(index)-2):
            #hd = hs[0] +':' +str(index[i]+2) +':' +str(index[i+2]+1) +':'+':'.join(hs[1:])
            hd = hs[0] +':' +str(index[i]+2) +':' +str(index[i+2]+1)
            ouFile.write(hd + '\n')
            ouFile.write(seq[index[i]+1:index[i+2]+1] + '\n')
    else:
        break
inFile.close()
ouFile.close()
