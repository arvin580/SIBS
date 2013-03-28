inFile = open('ERR0498-04-05.fastq')
ouFile = open('ERR0498-04-05.fastq.unique-num','w')

D = {}
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    line3 = inFile.readline()
    line4 = inFile.readline()
    if line1:
        D[line2]=1
    else:
        break
inFile.close()
ouFile.write('unique reads: '+ str(len(D))+'\n')
ouFile.close()

