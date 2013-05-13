import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 
import time
from matplotlib.path import Path
import matplotlib.patches as patches
import sys

gene = sys.argv[1]
GENE = {}
inFile = open('refGene-2013-04-22.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[12] == gene:
        GENE.setdefault(gene,[])
        pos = [fields[2],fields[3],int(fields[4]),int(fields[5]),int(fields[6]),int(fields[7])]
        starts = fields[9].split(',')
        ends = fields[10].split(',')
        for i in range(len(starts)-1):
            pos.append(int(starts[i]))
            pos.append(int(ends[i]))
        GENE[gene].append(pos)
inFile.close()
G = GENE[gene][0]
print(G)

G_len = G[3] - G[2]

fig = plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(-100,100 + G_len)
#ax.set_xticks([1, G[2]-G,G[3]])
ax.set_ylim(-1,1)
#ax.set_ylim(-0.6,1)

for i in range(6,len(G),2):
    start = G[i] - G[2]
    end = G[i+1] - G[2]
    verts = [
        (start, -0.1), # left, bottom
        (start, 0.1), # left, top
        (end,0.1), # right, top
        (end,-0.1), # right, bottom
        (0,0)
        ]

    codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='orange', lw=2)
    ax.add_patch(patch)


start = G[4] - G[2]
end = G[4] - G[2] + 1
verts = [
    (start, -0.2), # left, bottom
    (start, -0.1), # left, top
    (end,-0.1), # right, top
    (end,-0.2), # right, bottom
    (0,0)
    ]

codes = [Path.MOVETO,
     Path.LINETO,
     Path.LINETO,
     Path.LINETO,
     Path.CLOSEPOLY,
     ]
path = Path(verts, codes)
patch = patches.PathPatch(path, facecolor='red', lw=2)
ax.add_patch(patch)

start = G[5] - G[2]
end = G[5] - G[2] + 1
verts = [
    (start, -0.2), # left, bottom
    (start, -0.1), # left, top
    (end,-0.1), # right, top
    (end,-0.2), # right, bottom
    (0,0)
    ]

codes = [Path.MOVETO,
     Path.LINETO,
     Path.LINETO,
     Path.LINETO,
     Path.CLOSEPOLY,
     ]
path = Path(verts, codes)
patch = patches.PathPatch(path, facecolor='red', lw=2)
ax.add_patch(patch)




#### De
D = {}
inFile = open('split-mapped-deletion.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[0] == gene :
        for i in range(1,len(fields),29):
            pos1_query = int(fields[i+8])
            pos2_query = int(fields[i+9])
            pos3_query = int(fields[i+20])
            pos4_query = int(fields[i+21])
            pos1_subject = int(fields[i+10])
            pos2_subject = int(fields[i+11])
            pos3_subject = int(fields[i+22])
            pos4_subject = int(fields[i+23])
            if pos1_query + pos2_query < pos3_query +pos4_query:
                D.setdefault(pos2_subject,0)
                D[pos2_subject] +=  1
                D.setdefault(pos3_subject,0)
                D[pos3_subject] +=  1
            else:
                D.setdefault(pos4_subject,0)
                D[pos4_subject] +=  1
                D.setdefault(pos1_subject,0)
                D[pos1_subject] +=  1
inFile.close()
MAX = 0
for k in D:
    if D[k] > MAX:
        MAX = D[k]

for k in D:
    ax.scatter(k-G[2], D[k]/MAX+0.1,c='red',marker='o',edgecolors='')

#### In
D = {}
inFile = open('split-mapped-inversion.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[0] == gene :
        for i in range(1,len(fields),29):
            pos1_query = int(fields[i+8])
            pos2_query = int(fields[i+9])
            pos3_query = int(fields[i+20])
            pos4_query = int(fields[i+21])
            pos1_subject = int(fields[i+10])
            pos2_subject = int(fields[i+11])
            pos3_subject = int(fields[i+22])
            pos4_subject = int(fields[i+23])
            if pos1_query + pos2_query < pos3_query +pos4_query:
                D.setdefault(pos2_subject,0)
                D[pos2_subject] +=  1
                D.setdefault(pos3_subject,0)
                D[pos3_subject] +=  1
            else:
                D.setdefault(pos4_subject,0)
                D[pos4_subject] +=  1
                D.setdefault(pos1_subject,0)
                D[pos1_subject] +=  1
inFile.close()
MAX = 0
for k in D:
    if D[k] > MAX:
        MAX = D[k]

for k in D:
    ax.scatter(k-G[2], D[k]/MAX+0.2,c='red',marker='o',edgecolors='')

#### Du
D = {}
inFile = open('split-mapped-duplication.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[0] == gene :
        for i in range(1,len(fields),29):
            pos1_query = int(fields[i+8])
            pos2_query = int(fields[i+9])
            pos3_query = int(fields[i+20])
            pos4_query = int(fields[i+21])
            pos1_subject = int(fields[i+10])
            pos2_subject = int(fields[i+11])
            pos3_subject = int(fields[i+22])
            pos4_subject = int(fields[i+23])
            if pos1_query + pos2_query < pos3_query +pos4_query:
                D.setdefault(pos2_subject,0)
                D[pos2_subject] +=  1
                D.setdefault(pos3_subject,0)
                D[pos3_subject] +=  1
            else:
                D.setdefault(pos4_subject,0)
                D[pos4_subject] +=  1
                D.setdefault(pos1_subject,0)
                D[pos1_subject] +=  1
inFile.close()
MAX = 0
for k in D:
    if D[k] > MAX:
        MAX = D[k]

for k in D:
    ax.scatter(k-G[2], D[k]/MAX+0.3,c='red',marker='o',edgecolors='')



plt.savefig('HeLa-%s-diagram.pdf'%sys.argv[1])




'''
### add integration point
MAX = 20.0
L = []
inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-virus-site-region-unique2')
for line in inFile:
    line = line.strip()
    fields = line.split()
    L.append([fields[0],int(fields[1]),int(fields[2])])
inFile.close()
for item in L:
    if item[1] < 3000:
        ax.scatter(item[1], item[2]/MAX+0.1,c='red',marker='o',edgecolors='')
    else:
        ax.scatter(item[1], item[2]/MAX+0.1,edgecolors='')
### add HPV annotation
E6 = [(105,-0.3),(105,-0.2),(581,-0.2),(581,-0.3),(0,0)]
path = Path(E6, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.text((105+581)/2.0,-0.25,'E6',horizontalalignment='center',verticalalignment='center',fontsize=6)

E7 = [(590,-0.5),(590,-0.4),(907,-0.4),(907,-0.5),(0,0)]
path = Path(E7, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.text((590+907)/2.0,-0.45,'E7',horizontalalignment='center',verticalalignment='center',fontsize=6)

E1 = [(914,-0.3),(914,-0.2),(2887,-0.2),(2887,-0.3),(0,0)]
path = Path(E1, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.text((914+2887)/2.0,-0.25,'E1',horizontalalignment='center',verticalalignment='center',fontsize=6)

E2 = [(2817,-0.5),(2817,-0.4),(3914,-0.4),(3914,-0.5),(0,0)]
path = Path(E2, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.text((2817+3914)/2.0,-0.45,'E2',horizontalalignment='center',verticalalignment='center',fontsize=6)

E4 = [(3418,-0.3),(3418,-0.2),(3684,-0.2),(3684,-0.3),(0,0)]
path = Path(E4, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.text((3418+3684)/2.0,-0.25,'E4',horizontalalignment='center',verticalalignment='center',fontsize=6)

E5 = [(3936,-0.3),(3936,-0.2),(4157,-0.2),(4157,-0.3),(0,0)]
path = Path(E5, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.text((3936+4157)/2.0,-0.25,'E5',horizontalalignment='center',verticalalignment='center',fontsize=6)



L2 = [(4244,-0.5),(4244,-0.4),(5632,-0.4),(5632,-0.5),(0,0)]
path = Path(L2, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.text((4244+5632)/2.0,-0.45,'L2',horizontalalignment='center',verticalalignment='center',fontsize=6)

L1 = [(5430,-0.3),(5430,-0.2),(7136,-0.2),(7136,-0.3),(0,0)]
path = Path(L1, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.text((5430+7136)/2.0,-0.25,'L1',horizontalalignment='center',verticalalignment='center',fontsize=6)


ax.axes.get_yaxis().set_visible(False)


plt.savefig('HeLa-HPV18-integration-site-diagram.pdf')

'''
