dict1=dict()
inFile=open('sum_snv16sExome.exome_summary.indel.overall.filter')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    k='\t'.join(fields[21:26])
    dict1.setdefault(k,[0,0])
    dict1[k][0]=fields[2]
    dict1[k][1]=fields[8]
inFile.close()

def nonynonymous(iFile,d) :
    inFile=open(iFile)
    ouFile=open(iFile+'.frameshift','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])
        if d[k][0]!='nonframeshift' and d[k][0]!='unknown' :
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

nonynonymous('INDEL.exome.somatic.ICC4.not.repeat.mc',dict1)
nonynonymous('INDEL.exome.somatic.ICC5.not.repeat.mc',dict1)
nonynonymous('INDEL.exome.somatic.ICC9.not.repeat.mc',dict1)
nonynonymous('INDEL.exome.somatic.ICC10.not.repeat.mc',dict1)


nonynonymous('INDEL.exome.somatic.CHC5.not.repeat.mc',dict1)
nonynonymous('INDEL.exome.somatic.CHC6.not.repeat.mc',dict1)
nonynonymous('INDEL.exome.somatic.CHC7.not.repeat.mc',dict1)
nonynonymous('INDEL.exome.somatic.CHC10.not.repeat.mc',dict1)


