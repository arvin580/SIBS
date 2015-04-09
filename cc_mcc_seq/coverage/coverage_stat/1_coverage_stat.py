chr=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']


for sample in range(3,13) :
    for ch in chr :
        inFile=open('../fudan1.coverage')
        list1=list()
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            if fields[0].find(ch)!=-1 :
                list1.append(fields[sample])
        ouFile=open('fudan1.coverage.'+ch+'.'+str(sample-3),'w') 
        for item in list1 :
            ouFile.write(item+'\n')
        ouFile.close()

        inFile.close()
