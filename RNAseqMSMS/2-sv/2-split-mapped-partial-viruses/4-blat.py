import os
DIR = '.'
files = os.listdir(DIR)
for f in files:
    if f.find('.fasta')!=-1:
        ouFile = open(DIR+'/'+f.split('fasta')[0]+'blat.sh','w')
        ouFile.write('cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/\n')
        ouFile.write('db=/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta\n')
        ouFile.write('query='+f+'\n')
        ouFile.write('out=${query}.blated\n')
        #ouFile.write('blastn  -db $db  -query $query -out $out -outfmt 6\n')
        ouFile.write('blat $db $query  -out=blast8 $out\n')
        ouFile.close()
