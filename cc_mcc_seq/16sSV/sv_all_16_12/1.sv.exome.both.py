inFile = open('16s.sv.exome')
G = dict()
D = dict()

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0],[0,0])
    for i in range(1,17,2):
        D[fields[0]][0] += int(fields[i])
        G[fields[0]]=1
    for i in range(2,17,2):
        D[fields[0]][1] += int(fields[i])
        G[fields[0]]=1

inFile.close()

inFile = open('12s.sv.exome')
D2 = dict()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D2.setdefault(fields[0],[0,0])
    for i in range(1,13):
        D2[fields[0]][0] += int(fields[i])
        G[fields[0]]=1

inFile.close()

'''
for k in D :
    print(k)
    print(D[k])

for k in D2 :
    print(k)
    print(D2[k])
'''

from PyStats.PyStatsClass import PyStats
ps = PyStats()
ouFile = open('16s.12s.tumor.normal.sv.exome','w')
D3 = dict()
for k in G:
    #ouFile.write(k+'\t')
    #ouFile.write(str(D.get(k,[0,0])[0]+D2.get(k,[0,0])[0])+'\t')
    #ouFile.write(str(D.get(k,[0,0])[1]+D2.get(k,[0,0])[1])+'\n')
    D3.setdefault(k,[0,0,-1])
    D3[k][0] = D.get(k,[0,0])[0]+D2.get(k,[0,0])[0]
    D3[k][1] = D.get(k,[0,0])[1]+D2.get(k,[0,0])[1]
    D3[k][2] = ps.fisher_test([20,8,D3[k][0],D3[k][1]])

#for k in D3:
#    print(D3[k])

d = D3.items()
d.sort(cmp=lambda x,y:cmp(x[1][2],y[1][2]))
for items in d:
    ouFile.write(items[0]+'\t'+str(items[1][0])+'\t'+str(items[1][1])+'\t'+str(items[1][2])+'\n')
