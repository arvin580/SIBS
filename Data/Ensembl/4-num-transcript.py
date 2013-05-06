import sys
import re
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.transcript', 'w')
D = {}
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    if line1:
        s= re.search(r'transcript:(\w+)',line1)
        if s:
            #print(s.group(1))
            D.setdefault(s.group(1),0)
            D[s.group(1)]+=1
    else:
        break
inFile.close()

for k in D:
    ouFile.write(k+'\t'+str(D[k])+'\n')

ouFile.close()
