from PyPlot.PyPlotClass import *
a=PyPlot('split-mapped-deletion-inversion-duplication-translocation.gene.pdf')
#a.single_bar([84, 374, 1194, 3197],['4-types','3-types','2-types', '1-type'],yTitle='Number of Genes')
a.single_bar([950, 81, 858, 170],['Deletion','Duplication','Inversion', 'Translocation'],yTitle='Number of Genes')

