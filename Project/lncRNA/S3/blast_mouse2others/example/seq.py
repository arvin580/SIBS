import re
dict1=dict()
inFile1=open('/netshare1/home1/people/hansun/Project/lncRNA/S3/blast_mouse2others/lncrna_lncdb_mouse_genomic.fa')

for line in inFile1 :
    s=re.search(r'refGene_(NR_\w+)',line)
    if s :
        key=s.group(1)
    else :
        seq=line.strip()
        dict1[key]=seq
    
inFile1.close()
#print(dict1['NR_004444'])




file='NR_004444.grep'
inFile1=open(file)
row=0
for line in inFile :
    row+=1
    fields=line.split()
    query=dict1[fields[0]][int(fields[2])-1:int(fields[3])]
    inFile2=open('/netshare1/home1/people/hansun/Project/lncRNA/S3/blast_mouse2others/lncdb.mouse.%s.out'%fields[1])
    dict2=dict()
    flag=0
    for li in inFile2 :
        if flag==1 :

        if li==fields[] :
            flag=1


    inFile2.close()



inFile1.close()
