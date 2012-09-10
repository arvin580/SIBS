### python stat.py 
import sys
inFile1=open(sys.argv[1],'r')
seq=[]
for line in inFile1 :
    seq.append(line)
inFile1.close()

ouFile1=open(sys.argv[1]+'.seq.len','w')
seqlen=[]
for i in range(0,len(seq),2) :
    seqlen.append(len(seq[i+1])-1)

seqlen.sort()
ouFile1.write('\n'.join(str(i) for i in seqlen)+'\n')

ouFile1.close()




