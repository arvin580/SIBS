## python genelevel1.1.py snpindel_indel3030_raw.indel.recalibrated.annovar.exonic_variant_function

import sys

dict1={}
dict2={}
type=['frameshift insertion','frameshift deletion','nonframeshift insertion','nonframeshift deletion','stopgain SNV','stoploss SNV','unknown']
title=['gene_symbol','exonic_indel','new','dbsnp','new_frameshift_insertion','new_frameshift_deletion','new_nonframeshift_insertion','new_nonframeshift_deletion','new_stopgain_SNV','new_stoploss_SNV','new_unknown','dbsnp_frameshift_insertion','dbsnp_frameshift_deletion','dbsnp_nonframeshift_insertion','dbsnp_nonframeshift_deletion','dbsnp_stopgain_SNV','dbsnp_stoploss_SNV','dbsnp_unknown']
inFile1=open(sys.argv[1],'r')
ouFile1=open(sys.argv[1]+'.genelevel','w')
for line in inFile1 :
    fields=line.split('\t')
    gene=fields[2].split(':')[0]
    if fields[14]=='PASS' :
        dict1.setdefault(gene,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        dict1[gene][0]+=1
        if fields[10]=='.' :
            dict1[gene][1]+=1
            if fields[1]==type[0]:
                dict1[gene][3]+=1
            if fields[1]==type[1]:
                dict1[gene][4]+=1
            if fields[1]==type[2]:
                dict1[gene][5]+=1
            if fields[1]==type[3]:
                dict1[gene][6]+=1
            if fields[1]==type[4]:
                dict1[gene][7]+=1
            if fields[1]==type[5]:
                dict1[gene][8]+=1
            if fields[1]==type[6]:
                dict1[gene][9]+=1

        else :
            dict1[gene][2]+=1
            if fields[1]==type[0]:
                dict1[gene][10]+=1
            if fields[1]==type[1]:
                dict1[gene][11]+=1
            if fields[1]==type[2]:
                dict1[gene][12]+=1
            if fields[1]==type[3]:
                dict1[gene][13]+=1
            if fields[1]==type[4]:
                dict1[gene][14]+=1
            if fields[1]==type[5]:
                dict1[gene][15]+=1
            if fields[1]==type[6]:
                dict1[gene][16]+=1

ouFile1.write('\t'.join(title)+'\n')
for item in sorted(dict1.items(),key=lambda x:x[1][0],reverse=True) :
    ouFile1.write(item[0]+'\t'+'\t'.join(str(i) for i in item[1])+'\n')


inFile1.close()
ouFile1.close()


