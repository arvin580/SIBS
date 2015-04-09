## python genelevel2.py snpindel_snp3030_raw.snp.recalibrated.annovar.variant_function

import sys

dict1={}
type=['exonic;splicing','ncRNA_splicing','downstream','splicing','UTR5','ncRNA_exonic','intergenic','ncRNA_UTR5','intronic','ncRNA_UTR3','exonic','UTR3','upstream','UTR5;UTR3','upstream;downstream','ncRNA_intronic']
title=['gene_symbol','total_snv','new','dbsnp','new_exonic_splicing','new_ncRNA_splicing','new_downstream','new_splicing','new_UTR5','new_ncRNA_exonic','new_intergenic','new_ncRNA_UTR5','new_intronic','new_ncRNA_UTR3','new_exonic','new_UTR3','new_upstream','new_UTR5_UTR3','new_upstream_downstream','new_ncRNA_intronic','dbsnp_exonic_splicing','dbsnp_ncRNA_splicing','dbsnp_downstream','dbsnp_splicing','dbsnp_UTR5','dbsnp_ncRNA_exonic','dbsnp_intergenic','dbsnp_ncRNA_UTR5','dbsnp_intronic','dbsnp_ncRNA_UTR3','dbsnp_exonic','dbsnp_UTR3','dbsnp_upstream','dbsnp_UTR5','dbsnp_upstream_downstream','dbsnp_ncRNA_intronic']
inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.genelevel','w')
for line in inFile1 :
    fields=line.split('\t')
    gene=fields[1].split(':')[0]
    if fields[13]=='PASS' :
        dict1.setdefault(gene,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        dict1[gene][0]+=1
        if fields[9]=='.' :
            dict1[gene][1]+=1
            if fields[0]==type[0]:
                dict1[gene][3]+=1
            if fields[0]==type[1]:
                dict1[gene][4]+=1
            if fields[0]==type[2]:
                dict1[gene][5]+=1
            if fields[0]==type[3]:
                dict1[gene][6]+=1
            if fields[0]==type[4]:
                dict1[gene][7]+=1
            if fields[0]==type[5]:
                dict1[gene][8]+=1
            if fields[0]==type[6]:
                dict1[gene][9]+=1
            if fields[0]==type[7]:
                dict1[gene][10]+=1
            if fields[0]==type[8]:
                dict1[gene][11]+=1
            if fields[0]==type[9]:
                dict1[gene][12]+=1
            if fields[0]==type[10]:
                dict1[gene][13]+=1
            if fields[0]==type[11]:
                dict1[gene][14]+=1
            if fields[0]==type[12]:
                dict1[gene][15]+=1
            if fields[0]==type[13]:
                dict1[gene][16]+=1
            if fields[0]==type[14]:
                dict1[gene][17]+=1
            if fields[0]==type[15]:
                dict1[gene][18]+=1
        else :
            dict1[gene][2]+=1
            if fields[0]==type[0]:
                dict1[gene][19]+=1
            if fields[0]==type[1]:
                dict1[gene][20]+=1
            if fields[0]==type[2]:
                dict1[gene][21]+=1
            if fields[0]==type[3]:
                dict1[gene][22]+=1
            if fields[0]==type[4]:
                dict1[gene][23]+=1
            if fields[0]==type[5]:
                dict1[gene][24]+=1
            if fields[0]==type[6]:
                dict1[gene][25]+=1
            if fields[0]==type[7]:
                dict1[gene][26]+=1
            if fields[0]==type[8]:
                dict1[gene][27]+=1
            if fields[0]==type[9]:
                dict1[gene][28]+=1
            if fields[0]==type[10]:
                dict1[gene][29]+=1
            if fields[0]==type[11]:
                dict1[gene][30]+=1
            if fields[0]==type[12]:
                dict1[gene][31]+=1
            if fields[0]==type[13]:
                dict1[gene][32]+=1
            if fields[0]==type[14]:
                dict1[gene][33]+=1
            if fields[0]==type[15]:
                dict1[gene][34]+=1

ouFile1.write('\t'.join(title)+'\n')
for item in sorted(dict1.items(),key=lambda x:x[1][0],reverse=True) :
    ouFile1.write(item[0]+'\t'+'\t'.join(str(i) for i in item[1])+'\n')


inFile1.close()
ouFile1.close()


