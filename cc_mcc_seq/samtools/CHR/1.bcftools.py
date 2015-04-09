import os
import sys 
chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
        'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
        'chr18','chr19','chr20','chr21','chr22','chrX','chrY']
 
for d in [5,10,15,20,25,30,40,50]:

    for D in [100,150,200,250,300,400,500]:

        for ch in chrs:
            #cmd = 'bcftools view var.raw.%s.bcf | vcfutils.pl varFilter -d 20 -D 200 > var.flt.%s.vcf'%(ch,ch)
            cmd = 'bcftools view var.raw.%s.bcf | vcfutils.pl varFilter -d %s -D %s > var.flt.%s.vcf'%(ch,d,D,ch)
            os.system(cmd)
        
        head = 27
        num = [0] * 16
        num2 = [0] * 16
        somatic = [0] * 8 
        somatic2 = [0] * 8 
        for ch in chrs:
            f = 'var.flt.%s.vcf'%ch
            inFile=open(f)
            for n in range(head):
                line = inFile.readline()
            for line in inFile:
                line = line.strip()
                fields = line.split('\t')
                for i,item in enumerate(fields[-16:]):
                    if item.find('0/0') != 0:
                        if float(item.split(':')[-1])>20:
                            num[i]+=1
                        num2[i]+=1
                for i in range(-16, -8):
                    if fields[i].find('0/0') != 0 and fields[i+8].find('0/0') == 0 :
                        if float(fields[i].split(':')[-1])>20 and float(fields[i+8].split(':')[-1])>20:
                            somatic[i+16] += 1
                        somatic2[i+16] += 1
            inFile.close()

        print(str(d)+'\t'+str(D))
        print(num)
        print(somatic)
        print(num2)
        print(somatic2)




