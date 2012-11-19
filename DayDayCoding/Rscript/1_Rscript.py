R=r'''

a=c(12,3,4)
print(a)

'''
from Rscript.RscriptClass import Rscript
Rscript(R)
