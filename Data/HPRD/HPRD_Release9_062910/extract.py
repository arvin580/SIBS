inFile1=open('BINARY_PROTEIN_PROTEIN_INTERACTIONS.txt','r')

dict1=dict()
list1=list()
for line in inFile1 :
    fields=line.split('\t')
    dict1.setdefault(fields[0],0)
    list1.append(fields[0])
    dict1[fields[0]]+=1
    dict1.setdefault(fields[3],0)
    list1.append(fields[3])
    dict1[fields[3]]+=1
inFile1.close()
print(len(dict1))

set1=set()
set1=set(list1)


list2=list()
#inFile2=open('/netshare1/home1/szzhongxin/proj1/hansun/annotation/snpindel_snp3030/snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function.genelevel','r')
inFile2=open('/netshare1/home1/szzhongxin/proj1/hansun/annotation/snpindel2_snp3030/snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function.genelevel','r')

inFile2.readline()
for line in inFile2 :
    fields=line.split('\t')
    if int(fields[2])>=2 :
        list2.append(fields[0])
#    list2.append(fields[0])

inFile2.close()


set2=set()
set2=set(list2)
print(len(set2))

set3=set1 & set2
print(len(set3))


