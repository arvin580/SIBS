import os 
import re
os.chdir('Omssa')
files=os.listdir('.')

dict1=dict()
dict2=dict()

for file in files :
    s=re.search(r'fusionpoint$',file)
    if s :
        inFile=open(file)
        for line in inFile :
            fields=line.split(',')
            dict1.setdefault(fields[2],0)
            dict1[fields[2]]+=1

        inFile.close()

ouFile1=open('../omssa_fusion_point_0','w')
ouFile2=open('../omssa_fusion_point_2','w')

for key in dict1 :
    ouFile1.write(key+'\t'+str(dict1[key])+'\n')
    ouFile2.write(key+'\n')

ouFile1.close()
ouFile2.close()

     
for file in files :
    s=re.search(r'splicingpoint$',file)
    if s :
        inFile=open(file)
        for line in inFile :
            fields=line.split(',')
            dict2.setdefault(fields[2],0)
            dict2[fields[2]]+=1

        inFile.close()
2
ouFile1=open('../omssa_splicing_point_0','w')
ouFile2=open('../omssa_splicing_point_2','w')

for key in dict2 :
    ouFile1.write(key+'\t'+str(dict2[key])+'\n')
    ouFile2.write(key+'\n')

ouFile1.close()
ouFile2.close()





