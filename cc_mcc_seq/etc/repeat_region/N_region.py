### python repeat_region.py  
import sys
import os

inFile1=open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta','r')
ouFile1=open('N_region','w')



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
    dict2.setdefault(key,[0,0])
    dict2[key][0]=len(seq)
    i=0
    j=0
    while i<len(seq) :

        if seq[i]=='N' or seq[i]=='n':
            start=i
            j=i+1
            while j<len(seq) :
                if seq[j]!='N' and seq[j]!='n' :
                    end=j-1
                    i=j+1
                    x=ouFile1.write(key+'\t'+str(start+1)+'\t'+str(end+1)+'\t'+str(end-start+1)+'\n')
                    #print(key+'\t'+str(start+1)+'\t'+str(end+1)+'\t'+str(end-start+1))
                    dict2[key][1]+=eval('end-start+1')
                    break
                elif j==len(seq)-1 :
                    end=j
                    i=j+1
                    x=ouFile1.write(key+'\t'+str(start+1)+'\t'+str(end+1)+'\t'+str(end-start+1)+'\n')
                    dict2[key][1]+=eval('end-start+1')
                    break
                else :
                    j+=1
            if i==len(seq)-1 :
                end=i
                i+=1
                x=ouFile1.write(key+'\t'+str(start+1)+'\t'+str(end+1)+'\t'+str(end-start+1)+'\n')
                dict2[key][1]+=eval('end-start+1')
                break
        else :
            i+=1

for key in sorted(dict2) :
    print(key+'\t'+str(dict2[key][0])+'\t'+str(dict2[key][1])+'\t'+str(float(dict2[key][1])/float(dict2[key][0])))




        

