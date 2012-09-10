dict1=dict()
inFile=open('Retroviridae.mouse.out.anno')
for line in inFile :
    fields=line.split('\t')
    dict1[fields[0]]=1
inFile.close()

for key in dict1 :
    print(key)
