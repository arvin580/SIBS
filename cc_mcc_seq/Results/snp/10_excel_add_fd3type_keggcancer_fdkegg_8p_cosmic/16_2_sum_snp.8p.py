import os

os.chdir('exome')
inFile2=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg')
ouFile1=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p','w')

for line in inFile2 :
    line=line.strip('\r\n')
    fields=line.split('\t')
    if fields[28]=='chr8' and 1<=int(fields[29])<=45600000 :
        p8=['8p']
    else :
        p8=[]
    ouFile1.write(';'.join(p8)+'\t'+line+'\n')

inFile2.close()

