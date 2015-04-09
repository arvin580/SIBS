dict1=dict()
dict2=dict()
inFile=open('sum_snp.exome_summary.012')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    k='\t'.join(fields[21:26])
    dict1.setdefault(k,[0,0])
    dict1[k][0]=fields[2]
    dict1[k][1]=fields[8]
inFile.close()
inFile=open('sum_snp2.exome_summary.012')
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
    ouFile=open(iFile+'.nonsynonymous','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])
        if d[k][0]!='synonymous SNV' and d[k][0]!='unknown' :
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

nonynonymous('SNV.exome.somatic.ICC4',dict1)
nonynonymous('SNV.exome.somatic.ICC5',dict1)
nonynonymous('SNV.exome.somatic.ICC9',dict1)
nonynonymous('SNV.exome.somatic.ICC10',dict1)

nonynonymous('SNV.exome.somatic.ICC1',dict1)
nonynonymous('SNV.exome.somatic.ICC2',dict1)
nonynonymous('SNV.exome.somatic.ICC3',dict1)
nonynonymous('SNV.exome.somatic.ICC6',dict1)
nonynonymous('SNV.exome.somatic.ICC7',dict1)
nonynonymous('SNV.exome.somatic.ICC8',dict1)

nonynonymous('SNV.exome.somatic.CHC5',dict2)
nonynonymous('SNV.exome.somatic.CHC6',dict2)
nonynonymous('SNV.exome.somatic.CHC7',dict2)
nonynonymous('SNV.exome.somatic.CHC10',dict2)

nonynonymous('SNV.exome.somatic.CHC1',dict2)
nonynonymous('SNV.exome.somatic.CHC2',dict2)
nonynonymous('SNV.exome.somatic.CHC3',dict2)
nonynonymous('SNV.exome.somatic.CHC4',dict2)
nonynonymous('SNV.exome.somatic.CHC8',dict2)
nonynonymous('SNV.exome.somatic.CHC9',dict2)

