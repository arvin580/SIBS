#### python exon_type_split.py snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function
import sys

inFile1=open(sys.argv[1]+'.stat','r')
#ouFile1=open('haha','w')
F=[]

for line in inFile1 :
    fields=line.split('\t')
    if len(fields)==2 :
        FP=fields[0]
    if len(fields)==3 :
        NK=fields[1]
    if len(fields)==4 :
        TY=fields[2]
        L=[]
        L.append(FP)
        L.append(NK)
        L.append(TY)
        F.append(L)
inFile1.close()

for item in F :
    if item[0]== 'PASS' :
        ouFile1=open(sys.argv[1]+'_'+item[1]+'_'+item[2].replace(' ','_'),'w')
        inFile2=open(sys.argv[1],'r')
        for line in inFile2 :
            fields=line.split('\t')
            if fields[10]=='.':
                fields[10]='new'
            else :
                fields[10]='dbsnp'
            if fields[14]==item[0] and fields[10] ==item[1] and fields[1] ==item[2] :
                ouFile1.write(line)
        inFile2.close()
        ouFile1.close()


