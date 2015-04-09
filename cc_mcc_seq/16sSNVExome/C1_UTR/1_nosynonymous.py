dict1=dict()
inFile=open('sum_snv16sExome.genome_summary.overall.filter')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    k='\t'.join(fields[21:26])
    dict1.setdefault(k,[0,0])
    dict1[k][0]=fields[0]
    dict1[k][1]=fields[8]
inFile.close()

def nonynonymous(iFile,d) :
    inFile=open(iFile)
    ouFile=open(iFile+'.UTR','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])
        if d[k][0].find('UTR')!=-1:
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

nonynonymous('SNV.genome.somatic.ICC4.not.repeat.mc',dict1)
nonynonymous('SNV.genome.somatic.ICC5.not.repeat.mc',dict1)
nonynonymous('SNV.genome.somatic.ICC9.not.repeat.mc',dict1)
nonynonymous('SNV.genome.somatic.ICC10.not.repeat.mc',dict1)


nonynonymous('SNV.genome.somatic.CHC5.not.repeat.mc',dict1)
nonynonymous('SNV.genome.somatic.CHC6.not.repeat.mc',dict1)
nonynonymous('SNV.genome.somatic.CHC7.not.repeat.mc',dict1)
nonynonymous('SNV.genome.somatic.CHC10.not.repeat.mc',dict1)


