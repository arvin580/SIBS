import os
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse', 'w')
files = os.listdir('.')

for f in files:
    if f[-5:] == '.seq1':
        inFile = open(f)
        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            if line1:
                fields = line1.split('\t')
                if (fields[3].find('chr')==0 and fields[15].find('NC') == 0) or \
                        (fields[15].find('chr')==0 and fields[3].find('NC') == 0):
                    ouFile.write(line1+'\n')
                    ouFile.write(line2+'\n')
            else:
                break
        inFile.close()

