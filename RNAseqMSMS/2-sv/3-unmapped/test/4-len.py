import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.6acid','w')

while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        if len(seq) >=6 :
            #ouFile.write(':'.join(head.split(':')[0:3])+'\n')
            ouFile.write(head+'\n')
            ouFile.write(seq+'\n')
    else:
        break


inFile.close()
ouFile.close()

