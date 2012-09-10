inFile1=open('lncrna_ucsc_human_genomic_exonintron.fa','r')

ouFile1=open('lncrna_ucsc_human_genomic_exon.fa','w')
ouFile2=open('lncrna_ucsc_human_genomic_intron.fa','w')

list1=inFile1.readlines()

for i in range(1,len(list1),2) :
    if list1[i].isupper():
        ouFile1.write(list1[i-1])
        ouFile1.write(list1[i])
    elif list1[i].islower(): 
        ouFile2.write(list1[i-1])
        ouFile2.write(list1[i])
    else :
        print(list1[i-1])
        print(list1[i])
            


inFile1.close()

ouFile1.close()
ouFile2.close()
