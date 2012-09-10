inFile=open('he')
D=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    D.setdefault(fields[5],[])
    D[fields[5]].append(fields[0])
inFile.close()
for key in D :
    if len(D[key])>1 :
        print(key+'\t'+'\t'.join([str(x) for x in D[key]]))
