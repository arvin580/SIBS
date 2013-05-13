import os
DIR = '.'
files = os.listdir(DIR)
for f in files:
    if f[-3:] == '.fa':
        ouFile = open(DIR+'/'+f[0:-3]+'.blat.sh','w')
        ouFile.write('cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/2-split-mapped-splicing\n')
        ouFile.write('db=/netshare1/home1/people/hansun/Data/ucsc/refMrna-2013-5-13.fasta.fa\n')
        ouFile.write('query='+f+'\n')
        ouFile.write('out=${query}.blated\n')
        #ouFile.write('blastn  -db $db  -query $query -out $out -outfmt 6\n')
        ouFile.write('blat $db $query  -out=blast8 $out\n')
        ouFile.close()
