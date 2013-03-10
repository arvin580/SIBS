import os
files = os.listdir('.')
for f in files:
    if f[-4:]=='.srt':
        inFile = open(f)
        ouFile = open(f+'.txt','w')
        for line in inFile:
            line = line.strip()
            if line:
                if line.find('--')==-1:
                    try:
                        int(line)
                    except:
                        ouFile.write(line+'\n')
        inFile.close()
        ouFile.close()
