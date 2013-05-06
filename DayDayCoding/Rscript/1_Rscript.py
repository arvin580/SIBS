R=r'''

a=c(12,3,4)
print(a)
x = %s
y = %s

'''%(333,22)
from Rscript.RscriptClass import Rscript
#Rscript(R)
print(R)
