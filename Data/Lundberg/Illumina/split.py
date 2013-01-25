inFile = open('ERR0498-04-05.fastq')
ouFile1 = open('ERR0498-04-05.1.fastq','w')
ouFile2 = open('ERR0498-04-05.2.fastq','w')
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    line3 = inFile.readline()
    line4 = inFile.readline()
    line5 = inFile.readline()
    line6 = inFile.readline()
    line7 = inFile.readline()
    line8 = inFile.readline()
    if line1:
        ouFile1.write(line1)
        ouFile1.write(line2)
        ouFile1.write(line3)
        ouFile1.write(line4)
        ouFile2.write(line5)
        ouFile2.write(line6)
        ouFile2.write(line7)
        ouFile2.write(line8)
    else:
        break

inFile.close()
ouFile1.close()
ouFile2.close()
