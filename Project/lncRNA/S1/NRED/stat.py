inFile1=open('nred','r')
seqlen=[]
inFile1.readline()
for line in inFile1 :
    fields=line.split('\t')
    seqlen.append(len(fields[1]))
inFile1.close()


seqlen.sort()
print('\n'.join(str(i) for i in seqlen))
