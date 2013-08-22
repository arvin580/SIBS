D = {}
inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/hg19.chr.len')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = int(fields[1])
inFile.close()

chs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
        'chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']

def chr_site(inF,I):
    ouFile2 = open(inF+'-'+str(I),'w')
    ouFile = open(inF+'-'+str(I)+'-2','w')
    for ch in chs:
        #CHR = {}
        #for i in range(0,D[ch],I):
        #    CHR[str(i)+'\t'+str(i+I)]=0
        n = D[ch]/I+1
        CHR = [0]*n
        inFile = open(inF)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            if fields[0] == ch:
                #for k in CHR:
                #    if int(k.split('\t')[0])<=int(fields[1])<=int(k.split('\t')[1]):
                #        CHR[k]+=1
                m = int(fields[1])/I
                CHR[m] += 1
        inFile.close()
        #for k in CHR:
        #    ouFile.write(ch+'\t')
        #    ouFile.write(k+'\t')
        #    ouFile.write(str(CHR[k])+'\n')
        for i in range(len(CHR)):
            ouFile.write(ch+'\t')
            ouFile.write(str(i*I)+'\t')
            if I*(i+1)>D[ch]: 
                ouFile.write(str(D[ch])+'\t')
            else:
                ouFile.write(str((i+1)*I)+'\t')
            ouFile.write(str(CHR[i])+'\n')
        for i in range(len(CHR)):
            if CHR[i]>0:
                ouFile2.write(ch+'\t')
                ouFile2.write(str(i*I)+'\t')
                if I*(i+1)>D[ch]: 
                    ouFile2.write(str(D[ch])+'\t')
                else:
                    ouFile2.write(str((i+1)*I)+'\t')
                ouFile2.write(str(CHR[i])+'\n')
       
    ouFile.close()
    ouFile2.close()

chr_site('ERR0498-04-05.unmapped.unique.human-viruse-checked-more_than_one-human-chr-site',10000)    
chr_site('ERR0498-04-05.unmapped.unique.human-viruse-checked-more_than_one-human-chr-site',100000)    
   


'''
for ch in chs:
    L = [0]*D[ch]
    inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-chr-site')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0] == ch:
            L[int(fields[1])]+=1
    inFile.close()
    for i in range(len(L)) :
        if L[i] != 0:
            print(i)
            print(L[i])
'''    





