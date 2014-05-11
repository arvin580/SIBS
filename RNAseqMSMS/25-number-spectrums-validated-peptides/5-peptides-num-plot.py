D = {}
inFile = open('Peptides-Validated')
for line in inFile:
    line = line.strip()
    D.setdefault(line, [0, 0])
inFile.close()

inFile = open('Identified-Peptides-Corresponding-Reads2')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    peptide = fields[0]
    if peptide in D:
        D[peptide][0] = int(fields[1])
inFile.close()

inFile = open('Identified-Peptides-Corresponding-Spectrums')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    peptide = fields[0]
    if peptide in D:
        D[peptide][1] = int(fields[1])
inFile.close()

Read = []
Spectrum = []

import math

for k in D:
    Read.append(D[k][0])
    Spectrum.append(D[k][1])
    #Read.append(int(math.log(D[k][0],2)))
    #Spectrum.append(int(math.log(D[k][1],2)))

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax=fig.add_axes([0.1, 0.55, 0.8, 0.35])
#ax.hist(Spectrum,range(20) + [20,40,60,80,100,120,140,160])
ax.hist(Read,range(160))
ax.set_ylim(0,45)
ax.set_xticks(range(0,170,10))
ax.set_ylabel('Number of Peptides')
ax.set_xlabel('Number of Reads')
ax.xaxis.label.set_size(16)
ax.yaxis.label.set_size(16)
ax.set_title('Waiting exp. results, Not real data')

ax=fig.add_axes([0.1, 0.1, 0.8, 0.35])
ax.hist(Spectrum,range(160))
ax.set_ylim(0,45)
ax.set_xticks(range(0,170,10))
ax.set_ylabel('Number of Peptides')
ax.set_xlabel('Number of Spectra')
ax.xaxis.label.set_size(16)
ax.yaxis.label.set_size(16)
#ax.plot(Spectrum, '^')
plt.savefig('Peptides-Number-Reads-Spectra.pdf')
