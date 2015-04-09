import re
inFile1=open('snpindel_snp3030_raw.snp.recalibrated.annovar.variant_function','r')
lines=[0]

dict2=dict()
for line in inFile1 :
    fields=line.split('\t')
    #lines[0]+=1
    #lines.append(fields[0])
    dict2.setdefault(fields[3]+'\t'+fields[4],0)
    dict2[fields[3]+'\t'+fields[4]]+=1


inFile1.close()

#print(len(lines))

#dict1=dict()
#inFile2=open('snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function','r')
#
#for line in inFile2 :
#    fields=line.split('\t')
#    s=re.search(r'(\d+)$',fields[0])
#    if s :
#        dict1.setdefault(lines[int(s.group(1))],[])
#        dict1[lines[int(s.group(1))]].append(fields[0])
#inFile2.close()
#
#for key in dict1 :
#    print(key+'\t'+'\t'.join(dict1[key])+'\n')
for key in dict2 :
    print(key+'\t'+str(dict2[key])+'\n')
