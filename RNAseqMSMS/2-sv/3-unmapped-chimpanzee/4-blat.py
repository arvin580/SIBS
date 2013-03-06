import os
DIR = '.'
files = os.listdir(DIR)
for f in files:
    if f.find('.unmapped')!=-1:
        ouFile = open(DIR+'/'+f+'.blat.sh','w')
        ouFile.write('cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/3-unmapped-chimpanzee\n')
        ouFile.write('db=/netshare1/home1/people/hansun/Data/GenomeSeq/Chimpanzee/ucsc.chimpanzee.fasta\n')
        ouFile.write('query='+f+'\n')
        ouFile.write('out=${query}.blated\n')
        #ouFile.write('blastn  -db $db  -query $query -out $out -outfmt 6\n')
        ouFile.write('blat $db $query  -out=blast8 $out\n')
        ouFile.close()
