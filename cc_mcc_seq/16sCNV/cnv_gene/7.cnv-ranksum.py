from PyStats.PyStatsClass import *
def gene_two_group_ranksum_test(iFile,aList,bList) :
    ps=PyStats()
    ps.ranksum_test_file(iFile,aList,bList)

gene_two_group_ranksum_test('6.varScan.copynumber.called.depth_2_upper_down_gene',[-8,-7,-6,-5],[-4,-3,-2,-1])
gene_two_group_ranksum_test('6.varScan.copynumber.called.depth_1.5_upper_down_gene',[-8,-7,-6,-5],[-4,-3,-2,-1])
gene_two_group_ranksum_test('5.varScan.copynumber.called.depth_1.5_upper_down_gene',[-8,-7,-6,-5],[-4,-3,-2,-1])
gene_two_group_ranksum_test('5.varScan.copynumber.called.depth_2_upper_down_gene',[-8,-7,-6,-5],[-4,-3,-2,-1])

