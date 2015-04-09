inFile=open('/netshare1/home1/szzhongxin/proj1/hansun/Results/RNAseq/diff_RNA_isoform_CCC_AvsB.txt.sym')
dict1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=1
inFile.close()


inFile=open('/netshare1/home1/szzhongxin/proj1/hansun/Results/RNAseq/diff_RNA_isoform_MCC_AvsB.txt.sym')
dict2=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict2[fields[0]]=1
inFile.close()


inFile=open('/netshare1/home1/szzhongxin/proj1/hansun/Results/RNAseq/diff_RNA_isoform_CCCCvsMCC.txt.sym')
dict3=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict3[fields[0]]=1
inFile.close()

######################################





####################################
import re

inFile=open('sum_snp.exome_combined.sorted.pass012.new_cc_heat')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new_cc_heat_rna','w')
for line in inFile :
    line=line.rstrip('\n')
    fields=line.split('\t')
    s=re.split(r'[(,;]',fields[2])[0]
    print(s)
    flag='%s;%s;%s'%(dict1.get(s,0),dict2.get(s,0),dict3.get(s,0))
    ouFile.write(flag+'\t'+line+'\n')
inFile.close()
ouFile.close()

print('sum_snp.exome_combined.sorted.pass012.new_cc_heat_rna')


inFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc_heat')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc_heat_rna','w')
for line in inFile :
    line=line.rstrip('\n')
    fields=line.split('\t')
    s=re.split(r'[(,;]',fields[2])[0]
    print(s)
    flag='%s;%s;%s'%(dict1.get(s,0),dict2.get(s,0),dict3.get(s,0))
    ouFile.write(flag+'\t'+line+'\n')
inFile.close()
ouFile.close()

print('sum_snp.exome_combined.sorted.pass012.new_mcc_heat_rna')

inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.cc.genesorted_heat')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.cc.genesorted_heat_rna','w')
for line in inFile :
    line=line.rstrip('\n')
    fields=line.split('\t')
    s=re.split(r'[(,;]',fields[2])[0]
    print(s)
    flag='%s;%s;%s'%(dict1.get(s,0),dict2.get(s,0),dict3.get(s,0))
    ouFile.write(flag+'\t'+line+'\n')
inFile.close()
ouFile.close()

print('sum_snp.genome_combined.sorted.pass012.new.UTR.cc.genesorted_heat_rna')

inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.mcc.genesorted_heat')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.mcc.genesorted_heat_rna','w')
for line in inFile :
    line=line.rstrip('\n')
    fields=line.split('\t')
    s=re.split(r'[(,;]',fields[2])[0]
    print(s)
    flag='%s;%s;%s'%(dict1.get(s,0),dict2.get(s,0),dict3.get(s,0))
    ouFile.write(flag+'\t'+line+'\n')
inFile.close()
ouFile.close()

print('sum_snp.genome_combined.sorted.pass012.new.UTR.mcc.genesorted_heat_rna')

inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus_heat')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus_heat_rna','w')
for line in inFile :
    line=line.rstrip('\n')
    fields=line.split('\t')
    s=re.split(r'[(,;]',fields[10])[0]
    print(s)
    flag='%s;%s;%s'%(dict1.get(s,0),dict2.get(s,0),dict3.get(s,0))
    ouFile.write(flag+'\t'+line+'\n')
inFile.close()
ouFile.close()

print('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus_heat_rna')

inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus_heat')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus_heat_rna','w')
for line in inFile :
    line=line.rstrip('\n')
    fields=line.split('\t')
    s=re.split(r'[(,;]',fields[10])[0]
    print(s)
    flag='%s;%s;%s'%(dict1.get(s,0),dict2.get(s,0),dict3.get(s,0))
    ouFile.write(flag+'\t'+line+'\n')
inFile.close()
ouFile.close()

print('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus_heat_rna')

inFile=open('DNA_Sequencing_fd3type_heat')
ouFile=open('DNA_Sequencing_fd3type_heat_rna','w')
for line in inFile :
    line=line.rstrip('\n')
    fields=line.split('\t')
    s=re.split(r'[(,;]',fields[10])[0]
    print(s)
    flag='%s;%s;%s'%(dict1.get(s,0),dict2.get(s,0),dict3.get(s,0))
    ouFile.write(flag+'\t'+line+'\n')
inFile.close()
ouFile.close()

print('DNA_Sequencing_fd3type_heat_rna')

inFile=open('DNA_Sequencing_fd3type_UTR_heat')
ouFile=open('DNA_Sequencing_fd3type_UTR_heat_rna','w')
for line in inFile :
    line=line.rstrip('\n')
    fields=line.split('\t')
    s=re.split(r'[(,;]',fields[10])[0]
    print(s)
    flag='%s;%s;%s'%(dict1.get(s,0),dict2.get(s,0),dict3.get(s,0))
    ouFile.write(flag+'\t'+line+'\n')
inFile.close()
ouFile.close()
print('DNA_Sequencing_fd3type_UTR_heat_rna')





