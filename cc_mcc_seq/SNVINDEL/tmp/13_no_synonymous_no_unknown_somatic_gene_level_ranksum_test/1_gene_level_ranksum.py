from PyStats.PyStatsClass import *
def gene_two_group_ranksum_test(iFile,aList,bList) :
    ps=PyStats()
    ps.ranksum_test_file(iFile,aList,bList)

gene_two_group_ranksum_test('sum_snp.exome_summary.pass012.nonsynonymous.somatic.gene_level',[-8,-7,-6,-5],[-4,-3,-2,-1])
