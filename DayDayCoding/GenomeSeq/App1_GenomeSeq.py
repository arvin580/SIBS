from GenomeSeq.GenomeSeqClass import GenomeSeq 
gs=GenomeSeq()

#gs.make_false_normal_calling_out('sum_snp.exome_summary.csv','sum_snp34.exome_summary.csv',100)
#gs.make_false_normal_calling_out('sum_snp.genome_summary.csv','sum_snp34.genome_summary.csv',15000)

#gs.quality_pass_012_csv('sum_snp.exome_summary.csv',10)
#gs.quality_pass_012_csv('sum_snp2.exome_summary.csv',10)
#gs.quality_pass_012_csv('sum_snp34.exome_summary.csv',10)
##gs.quality_pass_012_csv('sum_snp34.exome_summary.csv',8)
#gs.quality_pass_012_csv('sum_snp.genome_summary.csv',10)
#gs.quality_pass_012_csv('sum_snp2.genome_summary.csv',10)
#gs.quality_pass_012_csv('sum_snp34.genome_summary.csv',10)
##gs.quality_pass_012_csv('sum_snp34.genome_summary.csv',8)


#gs.multi_calling_split('sum_snp.exome_summary.pass012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['ICC10A','ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A'])
#gs.multi_calling_split('sum_snp2.exome_summary.pass012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['CHC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A'])
#gs.multi_calling_split('sum_snp34.exome_summary.pass012',[-8,-7,-6,-5,-4,-3,-2,-1],['ICC10B','ICC4B','ICC5B','ICC9B','CHC10B','CHC5B','CHC6B','CHC7B'])
##gs.multi_calling_split('sum_snp34.exome_summary.pass012',[-8,-7,-6,-5,-4,-3,-2,-1],['ICC10B','ICC4B','ICC5B','ICC9B','CHC10B','CHC5B','CHC6B','CHC7B'])

#gs.multi_calling_split('sum_snp.genome_summary.pass012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['ICC10A','ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A'])
#gs.multi_calling_split('sum_snp2.genome_summary.pass012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['CHC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A'])
#gs.multi_calling_split('sum_snp34.genome_summary.pass012',[-8,-7,-6,-5,-4,-3,-2,-1],['ICC10B','ICC4B','ICC5B','ICC9B','CHC10B','CHC5B','CHC6B','CHC7B'])
##gs.multi_calling_split('sum_snp34.genome_summary.pass012',[-8,-7,-6,-5,-4,-3,-2,-1],['ICC10B','ICC4B','ICC5B','ICC9B','CHC10B','CHC5B','CHC6B','CHC7B'])

gs.tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.1A','sum_snp3.exome_summary.pass012.1B','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1AB')
gs.tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.4A','sum_snp3.exome_summary.pass012.4B','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.4AB')
gs.tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.5A','sum_snp3.exome_summary.pass012.5B','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.5AB')
gs.tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.9A','sum_snp3.exome_summary.pass012.9B','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.9AB')




#gs.combine_single_somatic(['sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.4AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.5AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.9AB'],'sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB')



#gs.select_no_synonymous_no_unknown('sum_snp.exome_summary.pass012')
#gs.select_no_synonymous_no_unknown('sum_snp2.exome_summary.pass012')
###gs.multi_calling_split('sum_snp.exome_summary.pass012.nonsynonymous',[-10],['10A'])
#gs.multi_calling_split('sum_snp.exome_summary.pass012.nonsynonymous',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['10A','1A','2A','3A','4A','5A','6A','7A','8A','9A'])
#gs.plot_snv_number([7058,8631,8542,8737,8735,8846,8791,8789,8933,7900])


#gs.snv_level_to_gene_level('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB',4)
#gs.gene_two_group_ranksum_test('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB.gene_level',[-4,-3,-2],[-3,-2,-1])
#gs.gene_two_group_ranksum_test_matshow('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB.gene_level',50,['1A','4A','5A','9A'])
#gs.gene_significant_mutated('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB.gene_level',[-4,-3,-2,-1])

#gs.venn_diagram('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.4AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.5AB',filename='set3.venn.pdf',setname1='tumor',setname2='normal',setname3='dbsnp')
#gs.venn_diagram('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.4AB',filename='set2.venn.pdf',setname1='tumor',setname2='dbsnp')


#d={'SAMD11  chr1    877831  877831  T       C       2':[1,2,3,4],'SAMD12  chr1    87731  87731  T       C       2':[3,4,5,6],'SAMD13  chr10    877831  877831  T       C       2':[5,6,7,8],'SAMD11  chr9    87781  87781  T       C       2':[10,11,12,13]}
#gs.sort_dict_by_chrom_postition(d,'haha')
