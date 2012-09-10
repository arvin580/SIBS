import sys
inFile=open(sys.argv[2])
ouFile1=open(sys.argv[2]+'_unmatched','w')
ouFile2=open(sys.argv[2]+'_matched','w')
dict1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if len(fields)==6 :
        dict1[fields[-1]]=0
inFile.close()

inFile=open(sys.argv[1])
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[2] not in dict1 :
        ouFile1.write(line+'\n')
    else :
        ouFile2.write(line+'\n')
inFile.close()
