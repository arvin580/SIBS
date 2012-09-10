dict1=dict()
inFile1=open('/netshare1/home1/people/hansun/Project/lncRNA/S3/lncrna_human_lncrnadb/lncrna_lncdb_human','r')


for line in inFile1 :
    fields=line.split()
    dict1[fields[1]]=fields[12]

inFile1.close()

import re
inFile2=open('blast_result2','r')
ouFile1=open('blast_result2.1','w')

line=inFile2.readline()
ouFile1.write('lncRNA.symbol'+'\t'+line)
for line in inFile2 :
    s=re.search(r'(NR_\w+)',line)
    if s :
        ouFile1.write(dict1[s.group(1)]+'\t'+line)




inFile2.close()
ouFile1.close()


