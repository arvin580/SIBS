flag={}
inFile=open('flag')
for line in inFile:
    line=line.strip()
    line=int(line)
    flag.setdefault(line,0)
    flag[line]+=1

ouFile = open('flag.out','w')
for key in flag:
    ouFile.write(str(key)+'\t'+str(flag[key])+'\n')

inFile.close()
ouFile.close()

