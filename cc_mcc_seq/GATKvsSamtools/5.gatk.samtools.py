inFile = open('snv.samtools.number')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    S_ICC4A=int(fields[0])
    S_ICC5A=int(fields[1])
    S_ICC9A=int(fields[2])
    S_ICC10A=int(fields[3])
    S_CHC5A=int(fields[4])
    S_CHC6A=int(fields[5])
    S_CHC7A=int(fields[6])
    S_CHC10A=int(fields[7])
    S_ICC4B=int(fields[8])
    S_ICC5B=int(fields[9])
    S_ICC9B=int(fields[10])
    S_ICC10B=int(fields[11])
    S_CHC5B=int(fields[12])
    S_CHC6B=int(fields[13])
    S_CHC7B=int(fields[14])
    S_CHC10B=int(fields[15])
inFile.close()

inFile = open('snv.gatk.number')
row = 0
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    row += 1
    if row == 1:
        G_ICC4A=int(fields[4])
        G_ICC5A=int(fields[5])
        G_ICC9A=int(fields[9])
        G_ICC10A=int(fields[0])
    if row == 2:
        G_CHC5A=int(fields[5])
        G_CHC6A=int(fields[6])
        G_CHC7A=int(fields[7])
        G_CHC10A=int(fields[0])
    if row == 3:
        G_ICC4B=int(fields[3])
        G_ICC5B=int(fields[4])
        G_ICC9B=int(fields[5])
        G_ICC10B=int(fields[2])
        G_CHC5B=int(fields[7])
        G_CHC6B=int(fields[8])
        G_CHC7B=int(fields[9])
        G_CHC10B=int(fields[6])

inFile.close()

Data=[[S_ICC4A,S_ICC4B,S_ICC5A,S_ICC5B,S_ICC9A,S_ICC9B,S_ICC10A,S_ICC10B,
       S_CHC5A,S_CHC5B,S_CHC6A,S_CHC6B,S_CHC7A,S_CHC7B,S_CHC10A,S_CHC10B],
[G_ICC4A,G_ICC4B,G_ICC5A,G_ICC5B,G_ICC9A,G_ICC9B,G_ICC10A,G_ICC10B,
       G_CHC5A,G_CHC5B,G_CHC6A,G_CHC6B,G_CHC7A,G_CHC7B,G_CHC10A,G_CHC10B]]

from PyPlot.PyPlotClass import *
pp=PyPlot('snv.number.pdf')
pp.multi_bar(Data,legTitle=['Samtools','GATK'],xLabel=['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B','CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B'],legX=0.85, legY=1)

