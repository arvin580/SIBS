def pass_truth(inF1,inF2,ouF) :
    D=dict()
    inFile=open(inF2)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[21:26])
        D[k]=fields[32]
    inFile.close()

    inFile=open(inF1)
    ouFile=open(ouF,'w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])
        if D[k]=='PASS' :
            ouFile.write(line+'\n')
    inFile.close()
    ouFile.close()

pass_truth('INDEL.exome.nopass.somatic.ICC4','sum_indel.exome_summary.012','INDEL.exome.somatic.ICC4')
pass_truth('INDEL.exome.nopass.somatic.ICC5','sum_indel.exome_summary.012','INDEL.exome.somatic.ICC5')
pass_truth('INDEL.exome.nopass.somatic.ICC9','sum_indel.exome_summary.012','INDEL.exome.somatic.ICC9')
pass_truth('INDEL.exome.nopass.somatic.ICC10','sum_indel.exome_summary.012','INDEL.exome.somatic.ICC10')


pass_truth('INDEL.exome.nopass.somatic.CHC5','sum_indel2.exome_summary.012','INDEL.exome.somatic.CHC5')
pass_truth('INDEL.exome.nopass.somatic.CHC6','sum_indel2.exome_summary.012','INDEL.exome.somatic.CHC6')
pass_truth('INDEL.exome.nopass.somatic.CHC7','sum_indel2.exome_summary.012','INDEL.exome.somatic.CHC7')
pass_truth('INDEL.exome.nopass.somatic.CHC10','sum_indel2.exome_summary.012','INDEL.exome.somatic.CHC10')


pass_truth('INDEL.genome.nopass.somatic.ICC4','sum_indel.genome_summary.012','INDEL.genome.somatic.ICC4')
pass_truth('INDEL.genome.nopass.somatic.ICC5','sum_indel.genome_summary.012','INDEL.genome.somatic.ICC5')
pass_truth('INDEL.genome.nopass.somatic.ICC9','sum_indel.genome_summary.012','INDEL.genome.somatic.ICC9')
pass_truth('INDEL.genome.nopass.somatic.ICC10','sum_indel.genome_summary.012','INDEL.genome.somatic.ICC10')


pass_truth('INDEL.genome.nopass.somatic.CHC5','sum_indel2.genome_summary.012','INDEL.genome.somatic.CHC5')
pass_truth('INDEL.genome.nopass.somatic.CHC6','sum_indel2.genome_summary.012','INDEL.genome.somatic.CHC6')
pass_truth('INDEL.genome.nopass.somatic.CHC7','sum_indel2.genome_summary.012','INDEL.genome.somatic.CHC7')
pass_truth('INDEL.genome.nopass.somatic.CHC10','sum_indel2.genome_summary.012','INDEL.genome.somatic.CHC10')

pass_truth('INDEL.exome.nopass.ICC4A','sum_indel.exome_summary.012','INDEL.exome.ICC4A')
pass_truth('INDEL.exome.nopass.ICC5A','sum_indel.exome_summary.012','INDEL.exome.ICC5A')
pass_truth('INDEL.exome.nopass.ICC9A','sum_indel.exome_summary.012','INDEL.exome.ICC9A')
pass_truth('INDEL.exome.nopass.ICC10A','sum_indel.exome_summary.012','INDEL.exome.ICC10A')

pass_truth('INDEL.exome.nopass.ICC4B','sum_indel34.exome_summary.012','INDEL.exome.ICC4B')
pass_truth('INDEL.exome.nopass.ICC5B','sum_indel34.exome_summary.012','INDEL.exome.ICC5B')
pass_truth('INDEL.exome.nopass.ICC9B','sum_indel34.exome_summary.012','INDEL.exome.ICC9B')
pass_truth('INDEL.exome.nopass.ICC10B','sum_indel34.exome_summary.012','INDEL.exome.ICC10B')

pass_truth('INDEL.exome.nopass.CHC5A','sum_indel2.exome_summary.012','INDEL.exome.CHC5A')
pass_truth('INDEL.exome.nopass.CHC6A','sum_indel2.exome_summary.012','INDEL.exome.CHC6A')
pass_truth('INDEL.exome.nopass.CHC7A','sum_indel2.exome_summary.012','INDEL.exome.CHC7A')
pass_truth('INDEL.exome.nopass.CHC10A','sum_indel2.exome_summary.012','INDEL.exome.CHC10A')

pass_truth('INDEL.exome.nopass.CHC5B','sum_indel34.exome_summary.012','INDEL.exome.CHC5B')
pass_truth('INDEL.exome.nopass.CHC6B','sum_indel34.exome_summary.012','INDEL.exome.CHC6B')
pass_truth('INDEL.exome.nopass.CHC7B','sum_indel34.exome_summary.012','INDEL.exome.CHC7B')
pass_truth('INDEL.exome.nopass.CHC10B','sum_indel34.exome_summary.012','INDEL.exome.CHC10B')



pass_truth('INDEL.genome.nopass.ICC4A','sum_indel.genome_summary.012','INDEL.genome.ICC4A')
pass_truth('INDEL.genome.nopass.ICC5A','sum_indel.genome_summary.012','INDEL.genome.ICC5A')
pass_truth('INDEL.genome.nopass.ICC9A','sum_indel.genome_summary.012','INDEL.genome.ICC9A')
pass_truth('INDEL.genome.nopass.ICC10A','sum_indel.genome_summary.012','INDEL.genome.ICC10A')

pass_truth('INDEL.genome.nopass.ICC4B','sum_indel34.genome_summary.012','INDEL.genome.ICC4B')
pass_truth('INDEL.genome.nopass.ICC5B','sum_indel34.genome_summary.012','INDEL.genome.ICC5B')
pass_truth('INDEL.genome.nopass.ICC9B','sum_indel34.genome_summary.012','INDEL.genome.ICC9B')
pass_truth('INDEL.genome.nopass.ICC10B','sum_indel34.genome_summary.012','INDEL.genome.ICC10B')

pass_truth('INDEL.genome.nopass.CHC5A','sum_indel2.genome_summary.012','INDEL.genome.CHC5A')
pass_truth('INDEL.genome.nopass.CHC6A','sum_indel2.genome_summary.012','INDEL.genome.CHC6A')
pass_truth('INDEL.genome.nopass.CHC7A','sum_indel2.genome_summary.012','INDEL.genome.CHC7A')
pass_truth('INDEL.genome.nopass.CHC10A','sum_indel2.genome_summary.012','INDEL.genome.CHC10A')

pass_truth('INDEL.genome.nopass.CHC5B','sum_indel34.genome_summary.012','INDEL.genome.CHC5B')
pass_truth('INDEL.genome.nopass.CHC6B','sum_indel34.genome_summary.012','INDEL.genome.CHC6B')
pass_truth('INDEL.genome.nopass.CHC7B','sum_indel34.genome_summary.012','INDEL.genome.CHC7B')
pass_truth('INDEL.genome.nopass.CHC10B','sum_indel34.genome_summary.012','INDEL.genome.CHC10B')


