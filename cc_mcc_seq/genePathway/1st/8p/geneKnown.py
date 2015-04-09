inFile1=open('snpindel12_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV.geneLevel.distribution','r')

mylist=list()
for line in inFile1 :
    fields=line.split()
    gene=fields[0]
    inFile2=open('/netshare1/home1/szzhongxin/proj1/hansun/annotation/exon_type/PASS_EXONIC_NONSYNONYMOUS/snpindel_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV','r')
    for li1 in inFile2 :
        snv=[0]*25
        li1=li1.strip()
        fields=li1.split('\t')
        if fields[2].split(':')[0]==gene :
            snv[0]=gene
            snv[1]=fields[3]
            snv[2]=fields[4]
            snv[3]=fields[6]
            snv[4]=fields[7]
            for i,item in enumerate(fields[-10:]) :
                if item.find('0/1')!=-1 or item.find('1/1')!=-1 or item.find('1/0')!=-1 :
                    snv[i+5]=1
            if sum(snv[5:15])>0 :
                mylist.append(snv)

    inFile2.close()
    inFile2=open('/netshare1/home1/szzhongxin/proj1/hansun/annotation/exon_type/PASS_EXONIC_NONSYNONYMOUS/snpindel2_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV','r')
    for li1 in inFile2 :
        snv=[0]*25
        li1=li1.strip()
        fields=li1.split('\t')
        if fields[2].split(':')[0]==gene :
            snv[0]=gene
            snv[1]=fields[3]
            snv[2]=fields[4]
            snv[3]=fields[6]
            snv[4]=fields[7]
            for i,item in enumerate(fields[-10:]) :
                if item.find('0/1')!=-1 or item.find('1/1')!=-1 or item.find('1/0')!=-1 :
                    snv[i+15]=1
            if sum(snv[15:25])>0 :
                mylist.append(snv)

    inFile2.close()

inFile1.close()
ouFile1=open('geneKnown','w')
for item in mylist :
    ouFile1.write('\t'.join([str(i) for i in item])+'\n')
ouFile1.close()


