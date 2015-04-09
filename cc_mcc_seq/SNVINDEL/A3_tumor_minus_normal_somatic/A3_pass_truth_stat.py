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
'''
pass_truth('SNV.exome.nopass.somatic.ICC4','sum_snp.exome_summary.012','SNV.exome.somatic.ICC4')
pass_truth('SNV.exome.nopass.somatic.ICC5','sum_snp.exome_summary.012','SNV.exome.somatic.ICC5')
pass_truth('SNV.exome.nopass.somatic.ICC9','sum_snp.exome_summary.012','SNV.exome.somatic.ICC9')
pass_truth('SNV.exome.nopass.somatic.ICC10','sum_snp.exome_summary.012','SNV.exome.somatic.ICC10')


pass_truth('SNV.exome.nopass.somatic.CHC5','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC5')
pass_truth('SNV.exome.nopass.somatic.CHC6','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC6')
pass_truth('SNV.exome.nopass.somatic.CHC7','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC7')
pass_truth('SNV.exome.nopass.somatic.CHC10','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC10')


pass_truth('SNV.genome.nopass.somatic.ICC4','sum_snp.genome_summary.012','SNV.genome.somatic.ICC4')
pass_truth('SNV.genome.nopass.somatic.ICC5','sum_snp.genome_summary.012','SNV.genome.somatic.ICC5')
pass_truth('SNV.genome.nopass.somatic.ICC9','sum_snp.genome_summary.012','SNV.genome.somatic.ICC9')
pass_truth('SNV.genome.nopass.somatic.ICC10','sum_snp.genome_summary.012','SNV.genome.somatic.ICC10')


pass_truth('SNV.genome.nopass.somatic.CHC5','sum_snp2.genome_summary.012','SNV.genome.somatic.CHC5')
pass_truth('SNV.genome.nopass.somatic.CHC6','sum_snp2.genome_summary.012','SNV.genome.somatic.CHC6')
pass_truth('SNV.genome.nopass.somatic.CHC7','sum_snp2.genome_summary.012','SNV.genome.somatic.CHC7')
pass_truth('SNV.genome.nopass.somatic.CHC10','sum_snp2.genome_summary.012','SNV.genome.somatic.CHC10')
'''

'''
pass_truth('SNV.exome.nopass.ICC4A','sum_snp.exome_summary.012','SNV.exome.ICC4A')
pass_truth('SNV.exome.nopass.ICC5A','sum_snp.exome_summary.012','SNV.exome.ICC5A')
pass_truth('SNV.exome.nopass.ICC9A','sum_snp.exome_summary.012','SNV.exome.ICC9A')
pass_truth('SNV.exome.nopass.ICC10A','sum_snp.exome_summary.012','SNV.exome.ICC10A')

pass_truth('SNV.exome.nopass.ICC4B','sum_snp34.exome_summary.012','SNV.exome.ICC4B')
pass_truth('SNV.exome.nopass.ICC5B','sum_snp34.exome_summary.012','SNV.exome.ICC5B')
pass_truth('SNV.exome.nopass.ICC9B','sum_snp34.exome_summary.012','SNV.exome.ICC9B')
pass_truth('SNV.exome.nopass.ICC10B','sum_snp34.exome_summary.012','SNV.exome.ICC10B')

pass_truth('SNV.exome.nopass.CHC5A','sum_snp2.exome_summary.012','SNV.exome.CHC5A')
pass_truth('SNV.exome.nopass.CHC6A','sum_snp2.exome_summary.012','SNV.exome.CHC6A')
pass_truth('SNV.exome.nopass.CHC7A','sum_snp2.exome_summary.012','SNV.exome.CHC7A')
pass_truth('SNV.exome.nopass.CHC10A','sum_snp2.exome_summary.012','SNV.exome.CHC10A')

pass_truth('SNV.exome.nopass.CHC5B','sum_snp34.exome_summary.012','SNV.exome.CHC5B')
pass_truth('SNV.exome.nopass.CHC6B','sum_snp34.exome_summary.012','SNV.exome.CHC6B')
pass_truth('SNV.exome.nopass.CHC7B','sum_snp34.exome_summary.012','SNV.exome.CHC7B')
pass_truth('SNV.exome.nopass.CHC10B','sum_snp34.exome_summary.012','SNV.exome.CHC10B')

'''


pass_truth('SNV.genome.nopass.ICC4A','sum_snp.genome_summary.012','SNV.genome.ICC4A')
pass_truth('SNV.genome.nopass.ICC5A','sum_snp.genome_summary.012','SNV.genome.ICC5A')
pass_truth('SNV.genome.nopass.ICC9A','sum_snp.genome_summary.012','SNV.genome.ICC9A')
pass_truth('SNV.genome.nopass.ICC10A','sum_snp.genome_summary.012','SNV.genome.ICC10A')

pass_truth('SNV.genome.nopass.ICC4B','sum_snp34.genome_summary.012','SNV.genome.ICC4B')
pass_truth('SNV.genome.nopass.ICC5B','sum_snp34.genome_summary.012','SNV.genome.ICC5B')
pass_truth('SNV.genome.nopass.ICC9B','sum_snp34.genome_summary.012','SNV.genome.ICC9B')
pass_truth('SNV.genome.nopass.ICC10B','sum_snp34.genome_summary.012','SNV.genome.ICC10B')

pass_truth('SNV.genome.nopass.CHC5A','sum_snp2.genome_summary.012','SNV.genome.CHC5A')
pass_truth('SNV.genome.nopass.CHC6A','sum_snp2.genome_summary.012','SNV.genome.CHC6A')
pass_truth('SNV.genome.nopass.CHC7A','sum_snp2.genome_summary.012','SNV.genome.CHC7A')
pass_truth('SNV.genome.nopass.CHC10A','sum_snp2.genome_summary.012','SNV.genome.CHC10A')

pass_truth('SNV.genome.nopass.CHC5B','sum_snp34.genome_summary.012','SNV.genome.CHC5B')
pass_truth('SNV.genome.nopass.CHC6B','sum_snp34.genome_summary.012','SNV.genome.CHC6B')
pass_truth('SNV.genome.nopass.CHC7B','sum_snp34.genome_summary.012','SNV.genome.CHC7B')
pass_truth('SNV.genome.nopass.CHC10B','sum_snp34.genome_summary.012','SNV.genome.CHC10B')


