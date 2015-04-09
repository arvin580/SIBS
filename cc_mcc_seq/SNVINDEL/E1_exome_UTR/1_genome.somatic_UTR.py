dict1=dict()
inFile=open('sum_snp.genome_summary.012')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    k='\t'.join(fields[21:26])
    dict1[k]=fields[0]
inFile.close()



def UTR(iFile1,iFile2):
    ouFile=open(iFile2+'.exome.UTR','w')
    inFile=open(iFile1)
    for line in inFile :
        ouFile.write(line)
    inFile.close()
    inFile=open(iFile2)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])
        if dict1[k].find('UTR')!=-1 :
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

UTR('SNV.exome.somatic.ICC10','SNV.genome.somatic.ICC10')
UTR('SNV.exome.somatic.ICC4','SNV.genome.somatic.ICC4')
UTR('SNV.exome.somatic.ICC5','SNV.genome.somatic.ICC5')
UTR('SNV.exome.somatic.ICC9','SNV.genome.somatic.ICC9')
#UTR('SNV.exome.somatic.CHC10','SNV.genome.somatic.CHC10')
#UTR('SNV.exome.somatic.CHC5','SNV.genome.somatic.CHC5')
#UTR('SNV.exome.somatic.CHC6','SNV.genome.somatic.CHC6')
#UTR('SNV.exome.somatic.CHC7','SNV.genome.somatic.CHC7')




