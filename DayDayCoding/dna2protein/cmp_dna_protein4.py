import sys

inFile=open(sys.argv[1])
ouFile=open(sys.argv[1]+'.find','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ids=fields[-1].split(';')
    if len(ids[0]) < 10 :
        for item in ids :
            ouFile.write('\t'.join(fields[0:-1])+'\t'+item+'\n')

inFile.close()
