import re
import sys

def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist



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
    elif pathway=='fudan' :
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

pathway=knowngene('/netshare1/home1/people/hansun/Data/KEGG/kegg_gene_symbol2','fudan')
inFile2=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer')
ouFile1=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg','w')

for line in inFile2 :
    line=line.strip('\r\n')
    fields=line.split('\t')
    if fields[7] in dict1 :
        fudankegg=dict1[fields[7]]
    else :
        fudankegg=[]
    ouFile1.write(';'.join(fudankegg)+'\t'+line+'\n')

inFile2.close()

