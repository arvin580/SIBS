inFile = open('qsub.sh')
L = []
for line in inFile:
    line = line.strip()
    L.append(line)
inFile.close()

n = 0
for k in range(0,len(L),10):
    n += 1
    ouFile = open('qsub-'+str(n)+'.sh','w')
    ouFile.write('cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/2-split-mapped-2\n')
    for i in range(10):
        if k+i < len(L):
            ouFile.write(L[k+i]+'\n')
    ouFile.close()
