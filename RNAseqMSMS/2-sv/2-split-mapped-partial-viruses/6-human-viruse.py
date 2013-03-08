import os
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse', 'w')
files = os.listdir('.')
for f in files:
    if f[-5:] == '.seq1':
        print(f)
        inFile = open(f)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            if (fields[3].find('chr')==0 and fields[15].find('NC') == 0) or \
                    (fields[15].find('chr')==0 and fields[3].find('NC') == 0):
                        ouFile.write(line+'\n')

        inFile.close()
