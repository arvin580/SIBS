def snv_distribution(iFile1,iFile2) :
    inFile=open(iFile2)
    dict1=dict()
    dict2=dict()
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        key='\t'.join(fields[21:26])
        dict1[key]=fields[0]+'\t'+fields[2]
    inFile.close()

    inFile=open(iFile1)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        key='\t'.join(fields[1:6])
        dict2.setdefault(dict1[key],0)
        dict2[dict1[key]]+=1
    ouFile=open(iFile1+'.dist','w')
    for key in dict2 :
        ouFile.write(key+'\t'+str(dict2[key])+'\n')
    ouFile.close()

snv_distribution('sum_snp.genome_summary.pass012.ICC4','sum_snp.genome_summary.pass012')
snv_distribution('sum_snp.genome_summary.pass012.ICC5','sum_snp.genome_summary.pass012')
snv_distribution('sum_snp.genome_summary.pass012.ICC9','sum_snp.genome_summary.pass012')
snv_distribution('sum_snp.genome_summary.pass012.ICC10','sum_snp.genome_summary.pass012')

snv_distribution('sum_snp.genome_summary.pass012.CHC5','sum_snp2.genome_summary.pass012')
snv_distribution('sum_snp.genome_summary.pass012.CHC6','sum_snp2.genome_summary.pass012')
snv_distribution('sum_snp.genome_summary.pass012.CHC7','sum_snp2.genome_summary.pass012')
snv_distribution('sum_snp.genome_summary.pass012.CHC10','sum_snp2.genome_summary.pass012')
