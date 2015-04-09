dict1=dict()
dict2=dict()
inFile=open('sum_indel.exome_summary.012')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    k='\t'.join(fields[21:26])
    dict1.setdefault(k,[0,0])
    dict1[k][0]=fields[2]
    dict1[k][1]=fields[8]
inFile.close()
inFile=open('sum_indel2.exome_summary.012')
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
    ouFile=open(iFile+'.frameshift_nondbsnp','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])
        if d[k][0].find('nonframeshift')==-1 and d[k][0].find('unknown')==-1 and d[k][1].find('rs')==-1 :
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

nonynonymous('INDEL.exome.somatic.ICC4',dict1)
nonynonymous('INDEL.exome.somatic.ICC5',dict1)
nonynonymous('INDEL.exome.somatic.ICC9',dict1)
nonynonymous('INDEL.exome.somatic.ICC10',dict1)


nonynonymous('INDEL.exome.somatic.CHC5',dict2)
nonynonymous('INDEL.exome.somatic.CHC6',dict2)
nonynonymous('INDEL.exome.somatic.CHC7',dict2)
nonynonymous('INDEL.exome.somatic.CHC10',dict2)


