### python filter.py ../lncrna_human_ucsc/lncrna_ucsc_human_genomic.fa ../lncrna_human_ucsc/lncrna_ucsc_human_mrna.fa ../lncrna_human_ucsc/lncrna_ucsc_human_genomic_exon.fa ../lncrna_human_ucsc/lncrna_ucsc_human_genomic_intron.fa ../lncrna_human_ucsc/lncrna_ucsc_human

dir='/netshare1/home1/people/hansun/Project/lncRNA/S2/lncRNAHuman/lncrna_human_ucsc/'
infile=['lncrna_ucsc_human_genomic.fa','lncrna_ucsc_human_mrna.fa','lncrna_ucsc_human_genomic_exon.fa','lncrna_ucsc_human_genomic_intron.fa','lncrna_ucsc_human']
oufile=['lncrna_lncdb_human_genomic.fa','lncrna_lncdb_human_mrna.fa','lncrna_lncdb_human_genomic_exon.fa','lncrna_lncdb_human_genomic_intron.fa','lncrna_lncdb_human']

import re


ouFile2=open(oufile[0],'w')
ouFile2.close()
ouFile2=open(oufile[1],'w')
ouFile2.close()
ouFile2=open(oufile[2],'w')
ouFile2.close()
ouFile2=open(oufile[3],'w')
ouFile2.close()
ouFile2=open(oufile[4],'w')
ouFile2.close()





inFile1=open('lncRNAdb_human_symbol_c2_mapped','r')

for line in inFile1 :
    fields=line.split()
    for item in fields[2:] :
        inFile2=open(dir+infile[0],'r')
        ouFile2=open(oufile[0],'a')
        lines=inFile2.readlines()
        for i in range(1,len(lines),2) :
            s=re.search(r'^>.*(NR_\d+)',lines[i-1])
            if s :
                if s.group(1)==item :
                    ouFile2.write(lines[i-1].strip()+' '+fields[0]+':'+fields[1]+':'+item+'\n')
                    ouFile2.write(lines[i])
        inFile2.close()
        ouFile2.close()

        inFile2=open(dir+infile[1],'r')
        ouFile2=open(oufile[1],'a')
        lines=inFile2.readlines()
        for i in range(1,len(lines),2) :
            s=re.search(r'^>.*(NR_\d+)',lines[i-1])
            if s :
                if s.group(1)==item :
                    ouFile2.write(lines[i-1].strip()+' '+fields[0]+':'+fields[1]+':'+item+'\n')
                    ouFile2.write(lines[i])
        inFile2.close()
        ouFile2.close()

        inFile2=open(dir+infile[2],'r')
        ouFile2=open(oufile[2],'a')
        lines=inFile2.readlines()
        for i in range(1,len(lines),2) :
            s=re.search(r'^>.*(NR_\d+)',lines[i-1])
            if s :
                if s.group(1)==item :
                    ouFile2.write(lines[i-1].strip()+' '+fields[0]+':'+fields[1]+':'+item+'\n')
                    ouFile2.write(lines[i])
        inFile2.close()
        ouFile2.close()

        inFile2=open(dir+infile[3],'r')
        ouFile2=open(oufile[3],'a')
        lines=inFile2.readlines()
        for i in range(1,len(lines),2) :
            s=re.search(r'^>.*(NR_\d+)',lines[i-1])
            if s :
                if s.group(1)==item :
                    ouFile2.write(lines[i-1].strip()+' '+fields[0]+':'+fields[1]+':'+item+'\n')
                    ouFile2.write(lines[i])
        inFile2.close()
        ouFile2.close()


        inFile2=open(dir+infile[4],'r')
        ouFile2=open(oufile[4],'a')
        for line in inFile2 :
            f=line.split()
            if f[1] == item :
                ouFile2.write(line)
        inFile2.close()
        ouFile2.close()

inFile1.close()
