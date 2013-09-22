import os
DIR = '.'
files = os.listdir(DIR)
L = []
for f in files:
    if f.find('.blat.sh')!=-1:
        L.append(f)

N = 20
for i in range(0,len(L),N):
    f = i/N
    ouFile= open(DIR+'/'+'qsub.'+str(f)+'.sh','w')
    for j in range(N):
        if i+j < len(L):
            #ouFile.write('qsub -q high '+L[i+j]+'\n')
            ouFile.write('qsub '+L[i+j]+'\n')
    ouFile.close()
