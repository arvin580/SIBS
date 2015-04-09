inFile=open('fudan1.coverage')
ouFile=open('fudan1.coverage.stat','w')
count=0
for line in inFile :
    fields=line.split('\t')
    if fields[3]=='0' :
        count+=1

inFile.close()
ouFile.write(str(count))
ouFile.close()

