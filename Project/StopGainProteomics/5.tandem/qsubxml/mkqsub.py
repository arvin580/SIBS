inFile = open('runtandem.pbs')
L = []
for line in inFile:
    L.append(line)
inFile.close()

for i in range(len(L)/60):
    ouFile = open('qsubtandem.'+str(i+1)+'.sh', 'w')
    ouFile.write('cd /netshare1/home1/people/hansun/StopGainProteomics/5.tandem\n')
    for j in range(60):
        x = i*60 + j
        ouFile.write(L[x])
    ouFile.close()

ouFile = open('qsubtandem.'+str(i+2)+'.sh', 'w')
ouFile.write('cd /netshare1/home1/people/hansun/StopGainProteomics/5.tandem\n')
for j in range(x+1,len(L)):
    ouFile.write(L[j])
ouFile.close()
        
        

