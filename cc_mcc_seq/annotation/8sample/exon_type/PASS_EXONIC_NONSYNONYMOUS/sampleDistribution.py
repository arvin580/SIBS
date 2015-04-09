#### python sampleDistribution.py snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV
#### python sampleDistribution.py snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV

import sys
import os

inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.distribution','w')

gt01=[0,0,0,0,0,0,0,0,0,0]
gt11=[0,0,0,0,0,0,0,0,0,0]
gt00=[0,0,0,0,0,0,0,0,0,0]
gt0111=[0,0,0,0,0,0,0,0,0,0]
dict01={}
dict11={}
dict00={}
dict0111={}
for line in inFile1 :
    line=line.strip()
    num01=0
    num11=0
    num00=0
    num0111=0
    fields=line.split('\t')
    for i in range(17,25):
        if fields[i].find('0/1')==0 :
            num01+=1
        if fields[i].find('1/1')==0 :
            num11+=1
        if fields[i].find('0/0')==0 :
            num00+=1
        if fields[i].find('0/1')==0 or fields[i].find('1/1')==0 :
            num0111+=1
    gt01[num01]+=1
    gt11[num11]+=1
    gt00[num00]+=1
    gt0111[num0111]+=1
    dict01.setdefault(num01,[])
    dict11.setdefault(num11,[])
    dict00.setdefault(num00,[])
    dict0111.setdefault(num0111,[])
    dict01[num01].append(line)
    dict11[num11].append(line)
    dict00[num00].append(line)
    dict0111[num0111].append(line)

inFile1.close()

#print(gt01)
#print(gt11)
#print(gt00)
#print(gt0111)
#print(dict0111[8])
for i in range(8,0,-1) :
    if i in dict0111 :
        for item in dict0111[i] :
            ouFile1.write(str(i)+'\t'+item+'\n')
ouFile1.close()

