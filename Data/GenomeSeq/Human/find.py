import  sys
import re
inFile=open('ucsc.hg19.fasta.fa')

file=inFile.read()

inFile.close()

s=re.findall(sys.argv[1],file,re.I)

print(s)





