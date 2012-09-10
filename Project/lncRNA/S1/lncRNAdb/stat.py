inFile1=open('lncRNAdbExportSeq.fa','r')
seq=[]
for line in inFile1 :
    seq.append(line)
inFile1.close()

seqlen=[]
ouFile1=open('human','w')
ouFile2=open('mouse','w')
ouFile3=open('rat','w')
ouFile4=open('other','w')
for i in range(0,len(seq),2) :
    seqlen.append(len(seq[i+1])-1)
    if seq[i].lower().find('human')!=-1 or seq[i].lower().find('homo')!=-1 :
        ouFile1.write(seq[i])
    elif seq[i].lower().find('mouse')!=-1 : 
        ouFile2.write(seq[i])
    elif seq[i].lower().find('rat')!=-1 : 
        ouFile3.write(seq[i])
    else :
        ouFile4.write(seq[i])




ouFile1.close()
ouFile2.close()
ouFile3.close()
ouFile4.close()

seqlen.sort()
print('\n'.join(str(i) for i in seqlen))




