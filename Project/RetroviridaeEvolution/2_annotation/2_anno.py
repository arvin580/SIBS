inFile=open('/netshare1/home1/people/hansun/Data/GenomeSeq/Mouse/mm9_refGene.txt')

dict1=dict()
for line in inFile :

    line=line.strip()
    fields=line.split('\t')
    dict1.setdefault(fields[12],[])
    dict1[fields[12]].append(fields[2:6])
    
inFile.close()

inFile=open('Retroviridae.mouse.out')
ouFile=open('Retroviridae.mouse.out.anno','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    chr=fields[1]
    start=int(fields[8])
    end=int(fields[9])

    list2=list()
    for key in dict1 :
        for item in dict1[key] :
            if item[0]==chr :
                if end<int(item[2]) or start>int(item[3]) :
                    pass
                else :
                    list2.append(key)
    ouFile.write(':'.join(set(list2))+'\t'+line+'\n')
        

inFile.close()
ouFile.close()
