#!/usr/bin/env python
import sys
inFile = open(sys.argv[1])
pfind = inFile.readlines()
inFile.close()

ouFile = open(sys.argv[1].split('.txt')[0]+'-pep','w')
i = 0
j = 0
while i < len(pfind):
    if pfind[i].find('Input=') == 0:
        spec = pfind[i].strip().split('Input=')[1]
        spec_info=[]
        NO1=[]
        NO1_SQ=[]
        NO2=[]
        NO2_SQ=[]
        NO3=[]
        NO3_SQ=[]
        NO4=[]
        NO4_SQ=[]
        j = i+1
        while pfind[j][0:2]!='NO':
            spec_info.append(pfind[j].strip())
            j += 1
        while pfind[j][0:3]=='NO1':
            NO1.append(pfind[j].strip())
            if pfind[j][0:7]=='NO1_SQ=':
                NO1_SQ.append(pfind[j].strip().split('NO1_SQ=')[1])
            j += 1
        while pfind[j][0:3]=='NO2':
            NO2.append(pfind[j].strip())
            if pfind[j][0:7]=='NO2_SQ=':
                NO2_SQ.append(pfind[j].strip().split('NO2_SQ=')[1])
            j += 1
        while pfind[j][0:3]=='NO3':
            NO3.append(pfind[j].strip())
            if pfind[j][0:7]=='NO3_SQ=':
                NO3_SQ.append(pfind[j].strip().split('NO3_SQ=')[1])
            j += 1
        while pfind[j][0:2]=='NO':
            NO4.append(pfind[j].strip())
            if pfind[j].find('SQ=')!=-1:
                NO4_SQ.append(pfind[j].strip().split('SQ=')[1])
            j += 1
        i = j -1
        ouFile.write(spec+'\t')
        if NO1:
            ouFile.write(':'.join(NO1_SQ)+'\t')
        else:
            ouFile.write(''+'\t')
        if NO2:
            ouFile.write(':'.join(NO2_SQ)+'\t')
        else:
            ouFile.write(''+'\t')
        if NO3:
            ouFile.write(':'.join(NO3_SQ)+'\t')
        else:
            ouFile.write(''+'\t')
        if NO4:
            ouFile.write(':'.join(NO4_SQ)+'\t')
        else:
            ouFile.write(''+'\t')
        ouFile.write('\t'.join(spec_info)+'\t')
        ouFile.write('\t'.join(NO1)+'\t')
        ouFile.write('\t'.join(NO2)+'\t')
        ouFile.write('\t'.join(NO3)+'\t')
        ouFile.write('\t'.join(NO4)+'\n')
    i += 1
ouFile.close()
