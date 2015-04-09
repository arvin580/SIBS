def somatic_cmp_dbindel(iFile1,iFile2) :
    dict1=dict()
    dict2=dict()
    inFile=open(iFile2)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[21:26])
        dict1[k]=fields[8]
        dict2[k]=fields[28]
    inFile.close()

    dbindel132=0
    dbindel135=0
    row=0

    inFile=open(iFile1)
    for line in inFile :
        row+=1
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:-1])
        if k in dict1:
            if dict1[k].find('rs')==0 :
                dbindel135+=1
            if dict2[k].find('rs')==0 :
                dbindel132+=1
    inFile.close()
    print(iFile1+'\t'+str(row)+'\t'+str(dbindel132)+'(%4.2f%%)'%(dbindel132/float(row)*100))+'\t'+str(dbindel135)+'(%4.2f%%)'%(dbindel135/float(row)*100)

somatic_cmp_dbindel('INDEL.genome.ICC4A','sum_indel.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.ICC5A','sum_indel.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.ICC9A','sum_indel.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.ICC10A','sum_indel.genome_summary.012')
#
somatic_cmp_dbindel('INDEL.genome.ICC4B','sum_indel34.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.ICC5B','sum_indel34.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.ICC9B','sum_indel34.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.ICC10B','sum_indel34.genome_summary.012')
##
somatic_cmp_dbindel('INDEL.genome.CHC5A','sum_indel2.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.CHC6A','sum_indel2.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.CHC7A','sum_indel2.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.CHC10A','sum_indel2.genome_summary.012')
##
somatic_cmp_dbindel('INDEL.genome.CHC5B','sum_indel34.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.CHC6B','sum_indel34.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.CHC7B','sum_indel34.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.CHC10B','sum_indel34.genome_summary.012')
##
##
somatic_cmp_dbindel('INDEL.genome.somatic.ICC4','sum_indel.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.somatic.ICC5','sum_indel.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.somatic.ICC9','sum_indel.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.somatic.ICC10','sum_indel.genome_summary.012')
##
##
somatic_cmp_dbindel('INDEL.genome.somatic.CHC5','sum_indel2.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.somatic.CHC6','sum_indel2.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.somatic.CHC7','sum_indel2.genome_summary.012')
somatic_cmp_dbindel('INDEL.genome.somatic.CHC10','sum_indel2.genome_summary.012')
