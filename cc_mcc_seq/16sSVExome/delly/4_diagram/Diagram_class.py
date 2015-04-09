from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Graphics import GenomeDiagram
#from Bio.Graphics.GenomeDiagram import rossLink
from reportlab.lib.units import cm
from reportlab.lib import colors


class Diagram :
    
    def __init__(self) :
        self.gdd = GenomeDiagram.Diagram('Diagram')
        self.gdt_features = self.gdd.new_track(1, greytrack=False)
        self.gds_features = self.gdt_features.new_set()
        self.start=1
        self.end=1000
        self.frag=1
        self.blast_num=0
        self.blast_rownum=10

    def Draw(self,file) :
        self.gdd.draw(format='linear', pagesize='A4', fragments=self.frag,start=self.start,end=self.end)
        self.gdd.write(file, "pdf")

    def Add_Anno(self,aList) :
        fields=aList.split()
        name=fields[1]
        chrom=fields[2]
        strand=fields[3]
        txStart=int(fields[4])
        self.txStart=txStart
        txEnd=int(fields[5])
        self.txEnd=txEnd
        self.frag=(txEnd-txStart)/10000
        self.end=txEnd-txStart
        cdsStart=int(fields[6])
        cdsEnd=int(fields[7])
        exonCount=int(fields[8])
        exonStarts=[int(i) for i in fields[9].split(',')[0:-1]]
        exonEnds=[int(i) for i in fields[10].split(',')[0:-1]]
        name2=fields[12]
        exonFrames=[int(i) for i in fields[15].split(',')[0:-1]]

        for i in range(exonCount):
    	    color = colors.linearlyInterpolatedColor(colors.red, colors.green,0,exonCount,i+1 )
	    feature = SeqFeature(FeatureLocation(exonStarts[i]-txStart,exonEnds[i]-txStart), strand=+1)
	    self.gds_features.add_feature(feature,name=str(i+1),label=True,color=color)

    def Add_Blast(self,aList) :
        self.blast_num+=1
        fields=aList.split('\t')
        gene=fields[0]
        query=fields[1]
        chrom=fields[2]
        q_start=int(fields[7])
        q_end=int(fields[8])
        s_start=int(fields[9])
        s_end=int(fields[10])
        evalue=fields[11]
        score=fields[12]

        color = colors.linearlyInterpolatedColor(colors.blue, colors.firebrick, 0,self.blast_rownum,self.blast_num)
        if s_start<=s_end:
            feature = SeqFeature(FeatureLocation(s_start-self.txStart,s_end-self.txStart), strand=-1)
        if s_start>s_end:
            feature = SeqFeature(FeatureLocation(s_end-self.txStart,s_start-self.txStart), strand=-1)
        self.gds_features.add_feature(feature,name=str(self.blast_num),label=True,color=color)

    def Set_Blast_RowNum(self,num) :
        self.blast_rownum=num
        




'''
d=Diagram()
inFile=open('ABL_human')
for line in inFile :
    line=line.strip()
    fields=line.split()
    if fields[12]=='ABL1' :
        d.Add_Anno(line)
        break
inFile.close()

d.Set_Blast_RowNum(row_num('ABL_NC'))

inFile=open('ABL_NC')
for line in inFile :
    line=line.strip()
    fields=line.split()
    if fields[0]=='ABL1' :
        d.Add_Blast(line)
inFile.close()

d.Draw('hh.pdf')
'''

