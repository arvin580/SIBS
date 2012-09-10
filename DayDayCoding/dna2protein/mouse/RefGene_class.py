import sys
import string
class RefGene :
    def __init__(self) :
        self.coding_position=[]
        self.coding_atcg=[]
        self.codon={'TTT':'F','TTC':'F','TCT':'S','TCC':'S','TAT':'Y','TAC':'Y','TGT':'C','TGC':'C','TTA':'L','TCA':'S','TAA':'*','TGA':'*','TTG':'L','TCG':'S','TAG':'*','TGG':'W','CTT':'L','CTC':'L','CCT':'P','CCC':'P','CAT':'H','CAC':'H','CGT':'R','CGC':'R','CTA':'L','CTG':'L','CCA':'P','CCG':'P','CAA':'Q','CAG':'Q','CGA':'R','CGG':'R','ATT':'I','ATC':'I','ACT':'T','ACC':'T','AAT':'N','AAC':'N','AGT':'S','AGC':'S','ATA':'I','ACA':'T','AAA':'K','AGA':'R','ATG':'M','ACG':'T','AAG':'K','AGG':'R','GTT':'V','GTC':'V','GCT':'A','GCC':'A','GAT':'D','GAC':'D','GGT':'G','GGC':'G','GTA':'V','GTG':'V','GCA':'A','GCG':'A','GAA':'E','GAG':'E','GGA':'G','GGG':'G'}

        ####
        ##calculate coding,noncoding,intergenic,intronic length, no strand difference
        #self.CodingDict=bsddb.btopen('a.bdb')
        #self.NonCodingDict=bsddb.btopen('b.bdb')
        #self.NonIntergenicDict=bsddb.btopen('c.bdb')
        #self.IntronicDict=bsddb.btopen('d.bdb')

        self.trans=string.maketrans('ATGCatgc','TACGtacg')
        ####

    def read_one_gene(self,aLine) :
        aLine=aLine.rstrip()
        fields=aLine.split('\t')
        self.aLine=aLine
        self.bin=fields[0]
        self.name=fields[1]
        self.chrom=fields[2]
        self.strand=fields[3]
        self.txStart=int(fields[4])
        self.txEnd=int(fields[5])
        self.cdsStart=int(fields[6])
        self.cdsEnd=int(fields[7])
        self.exonCount=int(fields[8])
        self.exonStarts=[int(i) for i in fields[9].split(',')[0:-1]]
        self.exonEnds=[int(i) for i in fields[10].split(',')[0:-1]]
        self.score=fields[11]
        self.name2=fields[12]
        self.cdsStartStat=fields[13]
        self.cdsEndStat=fields[14]
        self.exonFrames=[int(i) for i in fields[15].split(',')[0:-1]]

    def gene_to_coding(self) :
        if self.strand=='+' :
            for i in range(self.exonCount) :
                for j in range(self.exonStarts[i],self.exonEnds[i]) :
                    if self.cdsStart<=j<self.cdsEnd :
                        self.coding_position.append(j)
                        #sys.stdout.write('1')
                #sys.stdout.write('\n')
            
        if self.strand=='-' :
            for i in range(self.exonCount-1,-1,-1) :
                for j in range(self.exonEnds[i]-1,self.exonStarts[i]-1,-1) :
                    if self.cdsStart<=j<self.cdsEnd :
                        self.coding_position.append(j)
                        #sys.stdout.write('1')
                #sys.stdout.write('\n')
 
    def print_one_gene(self):
        print(self.bin)
        print(self.name)
        print(self.chrom)
        print(self.strand)
        print(self.txStart)
        print(self.txEnd)
        print(self.cdsStart)
        print(self.cdsEnd)
        print(self.exonCount)
        print('\t'.join(str(i) for i in self.exonStarts))
        print('\t'.join(str(i) for i in self.exonEnds))
        print(self.score)
        print(self.name2)
        print(self.cdsStartStat)
        print(self.cdsEndStat)
        print('\t'.join(str(i) for i in self.exonFrames))
    
    def position_to_atcg(self,chrom) :
        for item in self.coding_position :
            self.coding_atcg.append(chrom[item].upper())
            #self.coding_atcg.append(item)

    def is_coding(self,position) :
        if position in self.coding_position :
            return(1)
        else :
            return(0)

    def point_position(self,position) :
        for i,item in enumerate(self.coding_position) :
            if item == position :
                #return((i+1)/3+1)
                return(i/3+1)

    def point_change(self,position,frm,to) :
        coding_atcg_alt=self.coding_atcg[:]
        protein=[]
        protein_alt=[]
        for i,item in enumerate(self.coding_position) :
            if item==position :
                if coding_atcg_alt[i]==frm :
                    coding_atcg_alt[i]=to
                else :
                    sys.stderr.write('Warning(ref doesnt match):%s %s ref=%s yours=%s'%(self.chrom,position,coding_atcg_alt[i],frm)+'\t')
                    coding_atcg_alt[i]=to

        if position==self.coding_position[0] :

            if self.strand=='+' :
    
                for i in range(0,len(self.coding_position)-3,3) :
                #for i in range(0,len(self.coding_position),3) :
                    if position in self.coding_position[i:i+3] :
                        sys.stdout.write(self.chrom+'\t'+str(position)+'\t'+str(self.point_position(position))+'\t')
                        sys.stdout.write(''.join([str(x) for x in self.coding_atcg[i:i+3]])+'\t')
                        sys.stdout.write(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?')+'\t')
                        ####sys.stdout.write(''.join([str(x) for x in coding_atcg_alt[i:i+3]])+'\t')
                        ####sys.stdout.write(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?')+'\t')
    
                for i in range(0,len(self.coding_position)-3,3) :
                #for i in range(0,len(self.coding_position),3) :
                        #protein.append(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?'))
                        #protein_alt.append(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?'))
                        protein_alt.append(self.codon.get(''.join(coding_atcg_alt[i:i+3]),'?'))
                        protein.append(self.codon.get(''.join(self.coding_atcg[i:i+3]),'?'))
    
                ####sys.stdout.write(''.join(protein)+'\t')
                sys.stdout.write(''.join(protein)+'\n')
                ####sys.stdout.write(''.join(protein_alt)+'\n')
    
            if self.strand=='-' :
    
                for i in range(0,len(self.coding_position)-3,3) :
                #for i in range(0,len(self.coding_position),3) :
                    if position in self.coding_position[i:i+3] :
                        sys.stdout.write(self.chrom+'\t'+str(position)+'\t'+str(self.point_position(position))+'\t')
                        sys.stdout.write(''.join([str(x) for x in self.coding_atcg[i:i+3]])+'\t')
                        sys.stdout.write(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]).translate(self.trans),'?')+'\t')
                        ####sys.stdout.write(''.join([str(x) for x in coding_atcg_alt[i:i+3]])+'\t')
                        ####sys.stdout.write(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]).translate(self.trans),'?')+'\t')
    
                for i in range(0,len(self.coding_position)-3,3) :
                #for i in range(0,len(self.coding_position),3) :
                        #protein.append(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?'))
                        #protein_alt.append(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?'))
                        protein_alt.append(self.codon.get(''.join(coding_atcg_alt[i:i+3]).translate(self.trans),'?'))
                        protein.append(self.codon.get(''.join(self.coding_atcg[i:i+3]).translate(self.trans),'?'))
    
                ####sys.stdout.write(''.join(protein)+'\t')
                sys.stdout.write(''.join(protein)+'\n')
                ####sys.stdout.write(''.join(protein_alt)+'\n')

        else :

            if self.strand=='+' :
    
                for i in range(0,len(self.coding_position)-3,3) :
                #for i in range(0,len(self.coding_position),3) :
                    if position in self.coding_position[i:i+3] :
                        sys.stdout.write(self.chrom+'\t'+str(position)+'\t'+str(self.point_position(position))+'\t')
                        sys.stdout.write(''.join([str(x) for x in self.coding_atcg[i:i+3]])+'\t')
                        sys.stdout.write(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?')+'\n')
                        ####sys.stdout.write(''.join([str(x) for x in coding_atcg_alt[i:i+3]])+'\t')
                        ####sys.stdout.write(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?')+'\t')
    
                #for i in range(0,len(self.coding_position)-3,3) :
                #for i in range(0,len(self.coding_position),3) :
                        #protein.append(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?'))
                        #protein_alt.append(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?'))
                        #protein_alt.append(self.codon.get(''.join(coding_atcg_alt[i:i+3]),'?'))
                        #protein.append(self.codon.get(''.join(self.coding_atcg[i:i+3]),'?'))
    
                ####sys.stdout.write(''.join(protein)+'\t')
                #sys.stdout.write(''.join(protein)+'\n')
                ####sys.stdout.write(''.join(protein_alt)+'\n')
    
            if self.strand=='-' :
    
                for i in range(0,len(self.coding_position)-3,3) :
                #for i in range(0,len(self.coding_position),3) :
                    if position in self.coding_position[i:i+3] :
                        sys.stdout.write(self.chrom+'\t'+str(position)+'\t'+str(self.point_position(position))+'\t')
                        sys.stdout.write(''.join([str(x) for x in self.coding_atcg[i:i+3]])+'\t')
                        sys.stdout.write(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]).translate(self.trans),'?')+'\n')
                        ####sys.stdout.write(''.join([str(x) for x in coding_atcg_alt[i:i+3]])+'\t')
                        ####sys.stdout.write(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]).translate(self.trans),'?')+'\t')
    
                #for i in range(0,len(self.coding_position)-3,3) :
                #for i in range(0,len(self.coding_position),3) :
                        #protein.append(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?'))
                        #protein_alt.append(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?'))
                        #protein_alt.append(self.codon.get(''.join(coding_atcg_alt[i:i+3]).translate(self.trans),'?'))
                        #protein.append(self.codon.get(''.join(self.coding_atcg[i:i+3]).translate(self.trans),'?'))
    
                ####sys.stdout.write(''.join(protein)+'\t')
                #sys.stdout.write(''.join(protein)+'\n')
                ####sys.stdout.write(''.join(protein_alt)+'\n')


    def _point_change(self,position,frm,to) :
        coding_atcg_alt=self.coding_atcg[:]
        protein=[]
        protein_alt=[]
        for i,item in enumerate(self.coding_position) :
            if item==position :
                if coding_atcg_alt[i]==frm :
                    coding_atcg_alt[i]=to
                else :
                    sys.stderr.write('Warning(ref doesnt match):%s %s ref=%s yours=%s'%(self.chrom,position,coding_atcg_alt[i],frm)+'\t')
                    coding_atcg_alt[i]=to
        
        if self.strand=='+' :

            for i in range(0,len(self.coding_position)-3,3) :
            #for i in range(0,len(self.coding_position),3) :
                if position in self.coding_position[i:i+3] :
                    sys.stdout.write(self.chrom+'\t'+str(position)+'\t'+str(self.point_position(position))+'\t')
                    sys.stdout.write(''.join([str(x) for x in self.coding_atcg[i:i+3]])+'\t')
                    sys.stdout.write(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?')+'\t')
                    ####sys.stdout.write(''.join([str(x) for x in coding_atcg_alt[i:i+3]])+'\t')
                    ####sys.stdout.write(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?')+'\t')

            for i in range(0,len(self.coding_position)-3,3) :
            #for i in range(0,len(self.coding_position),3) :
                    #protein.append(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?'))
                    #protein_alt.append(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?'))
                    protein_alt.append(self.codon.get(''.join(coding_atcg_alt[i:i+3]),'?'))
                    protein.append(self.codon.get(''.join(self.coding_atcg[i:i+3]),'?'))

            ####sys.stdout.write(''.join(protein)+'\t')
            sys.stdout.write(''.join(protein)+'\n')
            ####sys.stdout.write(''.join(protein_alt)+'\n')

        if self.strand=='-' :

            for i in range(0,len(self.coding_position)-3,3) :
            #for i in range(0,len(self.coding_position),3) :
                if position in self.coding_position[i:i+3] :
                    sys.stdout.write(self.chrom+'\t'+str(position)+'\t'+str(self.point_position(position))+'\t')
                    sys.stdout.write(''.join([str(x) for x in self.coding_atcg[i:i+3]])+'\t')
                    sys.stdout.write(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]).translate(self.trans),'?')+'\t')
                    ####sys.stdout.write(''.join([str(x) for x in coding_atcg_alt[i:i+3]])+'\t')
                    ####sys.stdout.write(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]).translate(self.trans),'?')+'\t')

            for i in range(0,len(self.coding_position)-3,3) :
            #for i in range(0,len(self.coding_position),3) :
                    #protein.append(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?'))
                    #protein_alt.append(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?'))
                    protein_alt.append(self.codon.get(''.join(coding_atcg_alt[i:i+3]).translate(self.trans),'?'))
                    protein.append(self.codon.get(''.join(self.coding_atcg[i:i+3]).translate(self.trans),'?'))

            ####sys.stdout.write(''.join(protein)+'\t')
            sys.stdout.write(''.join(protein)+'\n')
            ####sys.stdout.write(''.join(protein_alt)+'\n')



    def print_coding_position(self) :
        for item in self.coding_position :
            print(item)

    def coding_length(self) :
        return len(self.coding_position)
    def gene_name(self) :
        return self.name2
        

    def first_coding_exon_frame(self) :
        if self.strand=='+' :
            for i in range(len(self.exonFrames)) :
                if self.exonFrames[i]!=-1 :
                    return self.exonFrames[i] 
        if self.strand=='-' :
            for i in range(len(self.exonFrames)-1,-1,-1) :
                if self.exonFrames[i]!=-1 :
                    return self.exonFrames[i] 
    def check_warning(self) :
        warning=0
        frame=self.first_coding_exon_frame()
        if frame!=0 :
            sys.stderr.write('Warning(the first coding exon frame is not 0) : \t')
            sys.stderr.write(self.aLine+'\n')
            warning=1

        coding_len=self.coding_length()
        if coding_len %3 !=0 :
            sys.stderr.write('Waring(coding len%3!=0) : \t')
            sys.stderr.write(self.aLine+'\n')
            warning=2
        return warning

    def _calculate_Coding_NoCoding_Intronic_Intergenic_Length(self) :
        if self.name.find('NM')==0 :
            self.NRNM+=1
            tmpDict=dict()
            for i in range(self.exonCount) :
                for j in range(self.exonStarts[i],self.exonEnds[i]) :
                    if self.cdsStart<=j<self.cdsEnd :
                        k=self.chrom+':'+str(j)
                        #self.CodingDict[k]=''
                        self.CodingDict.write(k+'\n')
                        tmpDict[k]=1

            for i in range(self.cdsStart,self.cdsEnd) :
                k=self.chrom+':'+str(i)
                if k not in tmpDict :
                    #self.IntronicDict[k]=''
                    self.IntronicDict.write(k+'\n')

            for i in range(self.txStart,self.cdsStart) :
                k=self.chrom+':'+str(i)
                #self.NonCodingDict[k]=''
                self.NonCodingDict.write(k+'\n')
            for i in range(self.cdsEnd,self.txEnd) :
                k=self.chrom+':'+str(i)
                #self.NonCodingDict[k]=''
                self.NonCodingDict.write(k+'\n')
        if self.name.find('NR')==0 :
            self.NRNM+=1
            for i in range(self.txStart,self.txEnd) :
                k=self.chrom+':'+str(i)
                #self.NonCodingDict[k]=''
                self.NonCodingDict.write(k+'\n')
        for i in range(self.txStart,self.txEnd) :
            k=self.chrom+':'+str(i)
            #self.NonIntergenicDict[k]=''
            self.NonIntergenicDict.write(k+'\n')

    def calculate_Coding_NoCoding_Intronic_Intergenic_Length(self) :
        import numpy as np
        dict1=dict()
        inFile1=open('hg19.chr.len')
        for line in inFile1 :
            line=line.strip()
            fields=line.split('\t')
            chr=fields[0]
            length=int(fields[1])
            dict1[chr]=length
        inFile1.close()

        ouFile=open('hg19.refGene.Coding_NoCoding_Intronic_Intergenic_Length','w')
        ouFile.write('chr'+'\t'+'total_len'+'\t'+'coding_len'+'\t'+'intron_len'+'\t'+'utr_len'+'\t'+'nr_len'+'\t'+'noncoding_len'+'\t'+'inter_len'+'\n')
        chrs=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14'
,'chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']
        for ch in chrs :
            chr=np.zeros((6,dict1[ch]))
            inFile=open('hg19_refGene.txt')
            #inFile=open('hg19_refGene.part.txt')
            for line in inFile :
                line=line.strip()
                self.read_one_gene(line)
                if self.chrom==ch :
                    if self.name.find('NM')==0 :
                        for i in xrange(self.exonCount) :
                            for j in xrange(self.exonStarts[i],self.exonEnds[i]) :
                                if self.cdsStart<=j<self.cdsEnd :
                                    chr[0][j]=1
                        for i in xrange(self.cdsStart,self.cdsEnd) :
                            if chr[0][i]==0 :
                                chr[1][i]=1

                        for i in xrange(self.txStart,self.cdsStart) :
                            chr[2][i]=1
                            chr[4][i]=1
                        for i in xrange(self.cdsEnd,self.txEnd) :
                            chr[2][i]=1
                            chr[4][i]=1

                    if self.name.find('NR')==0 :
                        for i in xrange(self.txStart,self.txEnd) :
                                chr[3][i]=1
                                chr[4][i]=1
                    for i in xrange(self.txStart,self.txEnd) :     
                        chr[5][i]=1
                        
        
            total_len=dict1[ch]
            coding_len=chr[0].sum()
            intron_len=chr[1].sum()
            utr_len=chr[2].sum()
            nr_len=chr[3].sum()
            noncoding_len=chr[4].sum()
            inter_len=total_len-chr[5].sum()
            ouFile.write(ch+'\t'+str(total_len)+'\t'+str(coding_len)+'\t'+str(intron_len)+'\t'+str(utr_len)+'\t'+str(nr_len)+'\t'+str(noncoding_len)+'\t'+str(inter_len)+'\n')
        ouFile.close()

        inFile=open('hg19.refGene.Coding_NoCoding_Intronic_Intergenic_Length')
        ouFile=open('hg19.refGene.Coding_NoCoding_Intronic_Intergenic_Length.total','w')
        line=inFile.readline()
        ouFile.write(line)

        chr_sum=[0]*8
        chr_sum[0]='total'
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            for i in range(len(fields[1:])) :
                chr_sum[i+1]+=float(fields[i+1])
            ouFile.write(line+'\n')
        inFile.close()

        ouFile.write('\t'.join([str(i) for i in chr_sum]))

    def is_in_region(self,chrom,start,end) :
        inFile=open('hg19_refGene.txt')
        for line in inFile :
            line=line.strip()
            self.read_one_gene(line)
            if self.chrom==chrom :
                if start<=self.txStart<=end or start<=self.txEnd<=end :
                    print(line)
        inFile.close()
        






