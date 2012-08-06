import re
inFile=open('mgffile')
ouFile=open('omssa.sh','w')

for line in inFile :
    line=line.strip()
    fields=line.split('/')
    out=fields[-1]
    out=re.sub('.MGF','.out',out)
    ouFile.write('/'.join(fields)+' '+'_'.join(fields[0:-1])+'_'+out+'\n')


ouFile.close()
inFile.close()
