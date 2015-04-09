dict1=dict()
def knowngene(file) :
    inFile1=open(file)
    for line in inFile1 :
        fields=line.split()
        for item in fields :
            dict1.setdefault(item,[])
            dict1[item].append(line)
    inFile1.close()
knowngene('/netshare1/home1/szzhongxin/proj1/hansun/genePathway/geneKnown/fudanexcel/gene_symbol_inflammation_found')
knowngene('/netshare1/home1/szzhongxin/proj1/hansun/genePathway/geneKnown/fudanexcel/gene_symbol_metastasis_found')
knowngene('/netshare1/home1/szzhongxin/proj1/hansun/genePathway/geneKnown/fudanexcel/gene_symbol_stemcell_found')

inFile2=open('snpindel12_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV.geneLevel.distribution','r')
ouFile1=open('snpindel12_snp3030_raw.snp.recalibrated.annovar.exonic_variant_function_new_nonsynonymous_SNV.geneLevel.distribution.knownGene','w')

for line in inFile2 :
    fields=line.split()
    if fields[0] in dict1 :
        ouFile1.write(line)
inFile2.close()

