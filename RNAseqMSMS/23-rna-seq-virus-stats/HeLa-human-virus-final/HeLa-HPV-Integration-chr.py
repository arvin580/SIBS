import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 
import time
from matplotlib.path import Path
import matplotlib.patches as patches

chr_MIN = 128000000
chr_MAX= 128800000
OFFSET = 10000
LEN = chr_MAX - chr_MIN + 1

fig = plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim(-OFFSET, OFFSET + LEN)
#ax.set_xticks([1]+range(1000,HPV_len+100,1000)+[HPV_len])
#ax.set_ylim(-1,1)
ax.set_ylim(-0.6,1)
### HPV 18
verts = [
    (0, -0.1), # left, bottom
    (0, 0.1), # left, top
    (LEN - 1,0.1), # right, top
    (LEN - 1,-0.1), # right, bottom
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

'''
### add integration point
MAX = 4.0
L = []
inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-virus-site-region-unique2-manual-edit')
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

'''
plt.savefig('HeLa-HPV-Integration-chr-diagram.pdf')


