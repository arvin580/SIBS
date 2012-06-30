import sys
class RefGene :
    def __init__(self) :
        self.coding_position=[]
        self.coding_atcg=[]
        self.codon={'TTT':'F','TTC':'F','TCT':'S','TCC':'S','TAT':'Y','TAC':'Y','TGT':'C','TGC':'C','TTA':'L','TCA':'S','TAA':'*','TGA':'*','TTG':'L','TCG':'S','TAG':'*','TGG':'W','CTT':'L','CTC':'L','CCT':'P','CCC':'P','CAT':'H','CAC':'H','CGT':'R','CGC':'R','CTA':'L','CTG':'L','CCA':'P','CCG':'P','CAA':'Q','CAG':'Q','CGA':'R','CGG':'R','ATT':'I','ATC':'I','ACT':'T','ACC':'T','AAT':'N','AAC':'N','AGT':'S','AGC':'S','ATA':'I','ACA':'T','AAA':'K','AGA':'R','ATG':'M','ACG':'T','AAG':'K','AGG':'R','GTT':'V','GTC':'V','GCT':'A','GCC':'A','GAT':'D','GAC':'D','GGT':'G','GGC':'G','GTA':'V','GTG':'V','GCA':'A','GCG':'A','GAA':'E','GAG':'E','GGA':'G','GGG':'G'}

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
                return((i+1)/3+1)

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

        for i in range(0,len(self.coding_position)-3,3) :
            if position in self.coding_position[i:i+3] :
                sys.stdout.write(str(position)+'\t'+str(self.point_position(position))+'\t')
                sys.stdout.write(''.join([str(x) for x in self.coding_atcg[i:i+3]])+'\t')
                sys.stdout.write(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?')+'\t')
                sys.stdout.write(''.join([str(x) for x in coding_atcg_alt[i:i+3]])+'\t')
                sys.stdout.write(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?')+'\t')

        for i in range(0,len(self.coding_position)-3,3) :
                #protein.append(self.codon.get(''.join([str(x) for x in self.coding_atcg[i:i+3]]),'?'))
                #protein_alt.append(self.codon.get(''.join([str(x) for x in coding_atcg_alt[i:i+3]]),'?'))
                protein_alt.append(self.codon.get(''.join(coding_atcg_alt[i:i+3]),'?'))
                protein.append(self.codon.get(''.join(self.coding_atcg[i:i+3]),'?'))

        sys.stdout.write(''.join(protein)+'\t')
        sys.stdout.write(''.join(protein_alt)+'\n')

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


            
        



