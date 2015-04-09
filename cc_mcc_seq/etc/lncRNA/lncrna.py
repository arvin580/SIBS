inFile1=open('lncrna_ucsc_human','r')

dict1=dict()
for line in inFile1 :
    fields=line.split()
    dict1.setdefault(fields[2],[fields[1],fields[3],fields[12]])
    dict1[fields[2]].append(fields[4])
    dict1[fields[2]].append(fields[5])

inFile1.close()

for key in dict1 :
    print(key+'\t'+'\t'.join(dict1[key]))



inFile2=open('/netshare1/home1/szzhongxin/proj1/hansun/annotation/snpindel_snp3030_raw.snp.recalibrated.vcf','r')

for i in range(125) :
    inFile2.readline()

for line in inFile2 :
    fields=line.split('\t')
    if fields[0] in dict1 :
        for p in range(3,len(dict1[fields[0]]),2) :
            if  dict1[fields[0]][p]<=fields[1]<=dict1[fields[0]][p+1] :
                print('\t'.join(fields[0:6])+'\t'+'\t'.join(dict1[fields[0]]))



inFile2.close()
