def select_no_synonymous_no_unknown(file) :
    inFile=open(file)
    ouFile=open(file+'.nonsynonymous','w')
    for line in inFile :
        line=line.rstrip()
        fields=line.split('\t')
        if fields[2]!='synonymous SNV' and fields[2]!='unknown' :
            ouFile.write(line+'\n')

    inFile.close()
    ouFile.close()


select_no_synonymous_no_unknown('sum_snp.exome_summary.pass012')
select_no_synonymous_no_unknown('sum_snp2.exome_summary.pass012')
select_no_synonymous_no_unknown('sum_snp34.exome_summary.pass012')
