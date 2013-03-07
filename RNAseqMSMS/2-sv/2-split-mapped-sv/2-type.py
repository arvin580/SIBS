import sys
import os
files = os.listdir('.')
ouFile1 = open('split-mapped-translocation','w')
ouFile2 = open('split-mapped-inversion','w')
ouFile3 = open('split-mapped-duplication','w')
ouFile4 = open('split-mapped-deletion','w')
for f in files:
    if f[-12:] =='not-splicing':
        inFile = open(f)

        while True:
            line1 = inFile.readline()
            line2 = inFile.readline()
            if line1:
                fields = line1.split()
                ch1 = fields[3]
                ch2 = fields[15]
                pos1 = int(fields[10])
                pos2 = int(fields[11])
                pos3 = int(fields[22])
                pos4 = int(fields[23])
                if ch1 != ch2:
                    ouFile1.write(line1)
                    ouFile1.write(line2)
                elif (pos1 - pos2)*(pos3-pos4) < 0:
                    ouFile2.write(line1)
                    ouFile2.write(line2)
                elif:
                    pass
                    


            else:
                break
        inFile.close()
