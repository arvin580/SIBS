inFile1=open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta','r')
dict1={}
for line in inFile1 :
    line=line.strip()
    if line.find('>')==0 :
        title=line
        title=title.strip('>')
        dict1[title]=[]
    else :  
        dict1[title].append(line)
inFile1.close()

for key in dict1 : 
    dict1[key]=''.join(dict1[key])
 

def interval_seq(chr,pos,before,after,type,alt) :
    if type==0 :
        return(dict1[chr][pos-before-1:pos+after])
    if type==1 :
        s=dict1[chr][pos-before-1:pos-1]+alt+dict1[chr][pos:pos+after]
        return(s)


pw=['hsa05200','hsa05202','hsa05210','hsa05211','hsa05212','hsa05213','hsa05214','hsa05215','hsa05216','hsa05217','hsa05218','hsa05219','hsa05220','hsa05221','hsa05222','hsa05223']
dict2=dict()
dict2['hsa05200']='Pathways in cancer'
dict2['hsa05202']='Transcriptional misregulation in cancer'
dict2['hsa05210']='Colorectal cancer'
dict2['hsa05211']='Renal cell carcinoma'
dict2['hsa05212']='Pancreatic cancer'
dict2['hsa05213']='Endometrial cancer'
dict2['hsa05214']='Glioma'
dict2['hsa05215']='Prostate cancer'
dict2['hsa05216']='Thyroid cancer'
dict2['hsa05217']='Basal cell carcinoma'
dict2['hsa05218']='Melanoma'
dict2['hsa05219']='Bladder cancer'
dict2['hsa05220']='Chronic myeloid leukemia'
dict2['hsa05221']='Acute myeloid leukemia'
dict2['hsa05222']='Small cell lung cancer'
dict2['hsa05223']='Non-small cell lung cancer'


def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist

import re
dict3=dict()

inFile1=open('/netshare1/home1/people/hansun/Data/KEGG/kegg_gene_symbol2')
for line in inFile1 :
    line=line.strip()
    fields=re.split(r'[\t:]',line)
    if fields[0] in  pw :
        for item in fields :
            dict3.setdefault(item,[])
            dict3[item].append(dict2[fields[0]])
inFile1.close()





inFile2=open('genePathway2','r')
ouFile1=open('genePathway3','w')
ouFile1.write('TYPE\tGENE\tCHR\tPOS\tREF\tALT\t')
ouFile1.write('10A\t1A\t2A\t3A\t4A\t5A\t6A\t7A\t8A\t9A\t')
ouFile1.write('M10A\tM1A\tM2A\tM3A\tM4A\tM5A\tM6A\tM7A\tM8A\tM9A\t')
ouFile1.write('REFSEQ(+-500bp)\t')
ouFile1.write('ALTSEQ(+-500bp)\n')


for line in inFile2 :
    line=line.strip()
    fields=line.split()

    ouFile1.write(';'.join(uniqueList(dict3[fields[0]]))+'\t'+line+'\t'+interval_seq(fields[1],int(fields[2]),500,500,0,fields[4])+'\t'+interval_seq(fields[1],int(fields[2]),500,500,1,fields[4])+'\n')

ouFile1.close()
inFile2.close()
