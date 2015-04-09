from PyPlot.PyPlotClass import *

def venn_diagram(iFile1,iFile2,iFile3=0,setname1='A',setname2='B',setname3='C',filename='test.pdf') :
    pp=PyPlot(filename)
    A=[]
    B=[]
    C=[]
    inFile1=open(iFile1)
    inFile2=open(iFile2)
    for line in inFile1 :
        line=line.strip()
        #fields=line.split('\t')
        A.append(line)
    for line in inFile2 :
        line=line.strip()
        #fields=line.split('\t')
        B.append(line)
    inFile1.close()
    inFile2.close()
    if iFile3==0 :
        pp.venn_diagram([set(A),set(B)],setname1,setname2)

    else :
        inFile3=open(iFile3)
        for line in inFile3 :
            line=line.strip()
            #fields=line.split('\t')
            C.append(line)
        inFile3.close()
        pp.venn_diagram([set(A),set(B),set(C)],setname1,setname2,setname3)


venn_diagram('sum_snp2.genome_summary.pass012.CHC10A','sum_snp34.genome_summary.pass012.CHC10B',filename='sum_snp.genome_summary.pass012.CHC10.pdf',setname1='CHC10A',setname2='CHC10B')
venn_diagram('sum_snp2.genome_summary.pass012.CHC5A','sum_snp34.genome_summary.pass012.CHC5B',filename='sum_snp.genome_summary.pass012.CHC5.pdf',setname1='CHC5A',setname2='CHC5B')
venn_diagram('sum_snp2.genome_summary.pass012.CHC6A','sum_snp34.genome_summary.pass012.CHC6B',filename='sum_snp.genome_summary.pass012.CHC6.pdf',setname1='CHC6A',setname2='CHC6B')
venn_diagram('sum_snp2.genome_summary.pass012.CHC7A','sum_snp34.genome_summary.pass012.CHC7B',filename='sum_snp.genome_summary.pass012.CHC7.pdf',setname1='CHC7A',setname2='CHC7B')


venn_diagram('sum_snp.genome_summary.pass012.ICC10A','sum_snp34.genome_summary.pass012.ICC10B',filename='sum_snp.genome_summary.pass012.ICC10.pdf',setname1='ICC10A',setname2='ICC10B')
venn_diagram('sum_snp.genome_summary.pass012.ICC4A','sum_snp34.genome_summary.pass012.ICC4B',filename='sum_snp.genome_summary.pass012.ICC4.pdf',setname1='ICC4A',setname2='ICC4B')
venn_diagram('sum_snp.genome_summary.pass012.ICC5A','sum_snp34.genome_summary.pass012.ICC5B',filename='sum_snp.genome_summary.pass012.ICC5.pdf',setname1='ICC5A',setname2='ICC5B')
venn_diagram('sum_snp.genome_summary.pass012.ICC9A','sum_snp34.genome_summary.pass012.ICC9B',filename='sum_snp.genome_summary.pass012.ICC9.pdf',setname1='ICC9A',setname2='ICC9B')
