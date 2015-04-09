### python repeat_region.py  
import sys
import os

inFile1=open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta','r')



dict1={}
for line in inFile1 :
    line=line.strip()
    if line.find('>')==0 :
        title=line
        title=title.strip('>')
        dict1[title]=[]
    else :  
        dict1[title].append(line)

inFile1.close()

for key in dict1 :
    dict1[key]=''.join(dict1[key])

dict2={}
for key in sorted(dict1) :
    seq=dict1[key]
    dict2.setdefault(key,[0,0,0,0,0,0,0])
    dict2[key][0]=len(seq)
    i=0
    while i<len(seq) :
        if seq[i]=='A' or seq[i]=='a' :
            dict2[key][1]+=1
        elif seq[i]=='T' or seq[i]=='t' :
            dict2[key][2]+=1
        elif seq[i]=='C' or seq[i]=='c' :
            dict2[key][3]+=1
        elif seq[i]=='G' or seq[i]=='g' :
            dict2[key][4]+=1
        elif seq[i]=='N' or seq[i]=='n' :
            dict2[key][5]+=1
        else :
            dict2[key][6]+=1
        i+=1

for key in sorted(dict2) :
    print(key+'\t'+str(dict2[key][0])+'\t'+str(dict2[key][1])+'\t'+str(dict2[key][2])+'\t'+str(dict2[key][3])+'\t'+str(dict2[key][4])+'\t'+str(dict2[key][5])+'\t'+str(dict2[key][6])+'\t'+str(float(dict2[key][1])/float(dict2[key][0]))+'\t'+str(float(dict2[key][2])/float(dict2[key][0]))+'\t'+str(float(dict2[key][3])/float(dict2[key][0]))+'\t'+str(float(dict2[key][4])/float(dict2[key][0]))+'\t'+str(float(dict2[key][5])/float(dict2[key][0]))+'\t'+str(float(dict2[key][6])/float(dict2[key][0])))




        

