###
import re

dict1=dict()

inFile1=open('lncRNAdb_mouse','r')
ouFile1=open('lncRNAdb_mouse_symbol','w')

for line in inFile1 :
    fields=re.split(r'[> _]',line)
    id=fields[1]
    dict1.setdefault(id,0)
    dict1[id]+=1
inFile1.close()

for key in dict1 :
    ouFile1.write(key+'\n')

ouFile1.close()
