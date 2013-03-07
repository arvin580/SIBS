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
                pos1 = float(fields[10])
                pos2 = float(fields[11])
                pos3 = float(fields[22])
                pos4 = float(fields[23])

                qpos1 = float(fields[8])
                qpos2 = float(fields[9])
                qpos3 = float(fields[20])
                qpos4 = float(fields[21])

                mid1 = (pos1+pos2)/2
                mid2 = (pos3+pos4)/2
                qmid1 = (qpos1+qpos2)/2
                qmid2 = (qpos3+qpos4)/2


                if ch1 != ch2:
                    ouFile1.write(line1)
                    ouFile1.write(line2)
                elif (pos1 - pos2)*(pos3-pos4) < 0:
                    ouFile2.write(line1)
                    ouFile2.write(line2)
                elif (mid1 - mid2)*(qmid1 - qmid2) < 0:
                    ouFile3.write(line1)
                    ouFile3.write(line2)
                    print(str(mid1)+'\t'+str(mid2)+'\t'+str(qmid1)+'\t'+str(qmid2))
                    


            else:
                break
        inFile.close()
