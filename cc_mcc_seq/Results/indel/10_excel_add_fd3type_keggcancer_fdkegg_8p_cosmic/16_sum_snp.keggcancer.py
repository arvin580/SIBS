import re
import sys

def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist



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


dict1=dict()
def knowngene(file,pathway='ALL') :
    if pathway=='ALL' :
        inFile1=open(file)
        for line in inFile1 :
            line=line.strip()
            fields=re.split(r'[\t:]',line)
            for item in fields :
                dict1.setdefault(item,[])
                dict1[item].append(fields[0])
        inFile1.close()
    elif pathway=='cancer' :
        inFile1=open(file)
        for line in inFile1 :
            line=line.strip()
            fields=re.split(r'[\t:]',line)
            if fields[0] in  pw :
                for item in fields :
                    dict1.setdefault(item,[])
                    dict1[item].append(dict2[fields[0]])
        inFile1.close()

    else :
        inFile1=open(file)
        for line in inFile1 :
            line=line.strip()
            fields=re.split(r'[\t:]',line)
            if fields[0] == pathway :
                for item in fields :
                    dict1.setdefault(item,[])
                    dict1[item].append(fields[0])
        inFile1.close()
    return pathway
pathway=knowngene('/netshare1/home1/people/hansun/Data/KEGG/kegg_gene_symbol2','cancer')

inFile2=open('sum_indel.exome_combined.sorted.pass012.new.genesorted.tpvalue.fd3type')
ouFile1=open('sum_indel.exome_combined.sorted.pass012.new.genesorted.tpvalue.fd3type.keggcancer','w')

for line in inFile2 :
    line=line.strip('\r\n')
    fields=line.split('\t')
    if fields[6] in dict1 :
        keggcancer=dict1[fields[6]]
    else :
        keggcancer=[]
    ouFile1.write(';'.join(keggcancer)+'\t'+line+'\n')

inFile2.close()
