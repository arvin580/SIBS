inFile1=open('raw.snp.recalibrated.vcf','r')
ouFile1=open('raw.snp.recalibrated.vcf.stat','w')

for j in range(125) :
    inFile1.readline()

n=[0]*22
for line in inFile1 :
    fields=line.split()

    #if fields[6]=='PASS' and fields[0].find('chrUn')==-1:
    if fields[6]=='PASS':

        if fields[2]=='.' :
            n[20]+=1
        else :
            n[21]+=1

        for i in range(-10,0,1) :
             if fields[i].find('0/1')!=-1 or fields[i].find('1/1')!=-1 or fields[i].find('1/0')!=-1 :
                if fields[2]=='.' :
                    n[i+10]+=1
                else :
                    n[i+20]+=1
inFile1.close()

for i in range(10):
    ouFile1.write(str(n[i])+'\t'+str(n[i+10])+'\t'+str(float(n[i])/float(n[i]+n[i+10]))+'\n')
ouFile1.write(str(n[20])+'\t'+str(n[21])+'\t'+str(float(n[20])/float(n[20]+n[21]))+'\n')
ouFile1.close()
