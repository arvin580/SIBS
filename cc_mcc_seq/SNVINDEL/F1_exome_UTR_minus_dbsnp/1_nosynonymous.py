dict1=dict()
dict2=dict()
inFile=open('sum_snp.genome_summary.012')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    k='\t'.join(fields[21:26])
    dict1.setdefault(k,[0,0])
    dict1[k][0]=fields[2]
    dict1[k][1]=fields[8]
inFile.close()
inFile=open('sum_snp2.genome_summary.012')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    k='\t'.join(fields[21:26])
    dict2.setdefault(k,[0,0])
    dict2[k][0]=fields[2]
    dict2[k][1]=fields[8]
inFile.close()


def nonynonymous(iFile,d) :
    inFile=open(iFile)
    ouFile=open(iFile+'.nondbsnp','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])
        if  d[k][1].find('rs')==-1 :
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

nonynonymous('SNV.genome.somatic.ICC10.exome.UTR',dict1)
nonynonymous('SNV.genome.somatic.ICC4.exome.UTR',dict1)
nonynonymous('SNV.genome.somatic.ICC5.exome.UTR',dict1)
nonynonymous('SNV.genome.somatic.ICC9.exome.UTR',dict1)


nonynonymous('SNV.genome.somatic.CHC10.exome.UTR',dict2)
nonynonymous('SNV.genome.somatic.CHC5.exome.UTR',dict2)
nonynonymous('SNV.genome.somatic.CHC6.exome.UTR',dict2)
nonynonymous('SNV.genome.somatic.CHC7.exome.UTR',dict2)


