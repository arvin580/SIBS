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

pass_truth('SNV.exome.nopass.somatic.ICC4','sum_snp.exome_summary.012','SNV.exome.somatic.ICC4')
pass_truth('SNV.exome.nopass.somatic.ICC5','sum_snp.exome_summary.012','SNV.exome.somatic.ICC5')
pass_truth('SNV.exome.nopass.somatic.ICC9','sum_snp.exome_summary.012','SNV.exome.somatic.ICC9')
pass_truth('SNV.exome.nopass.somatic.ICC10','sum_snp.exome_summary.012','SNV.exome.somatic.ICC10')

pass_truth('SNV.exome.nopass.somatic.ICC1','sum_snp.exome_summary.012','SNV.exome.somatic.ICC1')
pass_truth('SNV.exome.nopass.somatic.ICC2','sum_snp.exome_summary.012','SNV.exome.somatic.ICC2')
pass_truth('SNV.exome.nopass.somatic.ICC3','sum_snp.exome_summary.012','SNV.exome.somatic.ICC3')
pass_truth('SNV.exome.nopass.somatic.ICC6','sum_snp.exome_summary.012','SNV.exome.somatic.ICC6')
pass_truth('SNV.exome.nopass.somatic.ICC7','sum_snp.exome_summary.012','SNV.exome.somatic.ICC7')
pass_truth('SNV.exome.nopass.somatic.ICC8','sum_snp.exome_summary.012','SNV.exome.somatic.ICC8')


pass_truth('SNV.exome.nopass.somatic.CHC5','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC5')
pass_truth('SNV.exome.nopass.somatic.CHC6','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC6')
pass_truth('SNV.exome.nopass.somatic.CHC7','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC7')
pass_truth('SNV.exome.nopass.somatic.CHC10','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC10')

pass_truth('SNV.exome.nopass.somatic.CHC1','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC1')
pass_truth('SNV.exome.nopass.somatic.CHC2','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC2')
pass_truth('SNV.exome.nopass.somatic.CHC3','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC3')
pass_truth('SNV.exome.nopass.somatic.CHC4','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC4')
pass_truth('SNV.exome.nopass.somatic.CHC8','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC8')
pass_truth('SNV.exome.nopass.somatic.CHC9','sum_snp2.exome_summary.012','SNV.exome.somatic.CHC9')
