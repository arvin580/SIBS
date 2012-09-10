from Bio import SeqIO
import os
import re

home='/home/hanice/Data/RetroviridaeGenome'
for item in os.listdir(home) :
    if os.path.isdir(home+os.sep+item) :
        os.chdir(home+os.sep+item)
        for it in os.listdir('.') :
            s=re.search(r'.gbk$',it)
            if s :
                SeqIO.convert(it, "genbank",'../'+it+'.fna', "fasta")
