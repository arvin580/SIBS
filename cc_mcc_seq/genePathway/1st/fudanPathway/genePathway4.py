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


pw=['hsa00010','hsa00020','hsa00270','hsa03018','hsa04010','hsa04012','hsa04060','hsa04062','hsa04110','hsa04115','hsa04150','hsa04210','hsa04310','hsa04320','hsa04360','hsa04370','hsa04380','hsa04510','hsa04514','hsa04520','hsa04530','hsa04540','hsa04620','hsa04621','hsa04630','hsa04640','hsa04660','hsa04662','hsa04976','hsa05145','hsa05152','hsa05160','hsa05162','hsa05200','hsa05211','hsa05212','hsa05219','hsa05220','hsa05221','hsa05223','hsa05323','hsa05340']


dict2=dict()

dict2['hsa00010']='Glycolysis'
dict2['hsa00020']='Citrate cycle (TCA cycle)'
dict2['hsa00270']='Cysteine and methionine metabolism'
dict2['hsa03018']='RNA degradation'
dict2['hsa04010']='MAPK signaling pathway'
dict2['hsa04012']='ErbB signaling pathway'
dict2['hsa04060']='Cytokine-cytokine receptor interaction'
dict2['hsa04062']='Chemokine signaling pathway'
dict2['hsa04110']='Cell cycle'
dict2['hsa04115']='p53 signaling pathway'
dict2['hsa04150']='mTOR signaling pathway'
dict2['hsa04210']='Apoptosis'
dict2['hsa04310']='Wnt signaling pathway'
dict2['hsa04320']='Dorso-ventral axis formation'
dict2['hsa04360']='Axon guidance'
dict2['hsa04370']='VEGF signaling pathway'
dict2['hsa04380']='Osteoclast differentiation'
dict2['hsa04510']='Focal adhesion'
dict2['hsa04514']='Cell adhesion molecules (CAMs)'
dict2['hsa04520']='Adherens junction'
dict2['hsa04530']='Tight junction'
dict2['hsa04540']='Gap junction'
dict2['hsa04620']='Toll-like receptor signaling pathway'
dict2['hsa04621']='NOD-like receptor signaling pathway'
dict2['hsa04630']='Jak-STAT signaling pathway'
dict2['hsa04640']='Hematopoietic cell lineage'
dict2['hsa04660']='T cell receptor signaling pathway'
dict2['hsa04662']='B cell receptor signaling pathway'
dict2['hsa04976']='Bile secretion'
dict2['hsa05145']='Toxoplasmosis'
dict2['hsa05152']='Tuberculosis'
dict2['hsa05160']='Hepatitis C'
dict2['hsa05162']='Measles'
dict2['hsa05200']='Pathways in cancer'
dict2['hsa05211']='Renal cell carcinoma'
dict2['hsa05212']='Pancreatic cancer'
dict2['hsa05219']='Bladder cancer'
dict2['hsa05220']='Chronic myeloid leukemia'
dict2['hsa05221']='Acute myeloid leukemia'
dict2['hsa05223']='Non-small cell lung cancer'
dict2['hsa05323']='Rheumatoid arthritis'
dict2['hsa05340']='Primary immunodeficiency'

















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
