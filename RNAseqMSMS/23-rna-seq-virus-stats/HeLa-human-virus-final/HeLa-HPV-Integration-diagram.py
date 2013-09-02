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
ax=fig.add_subplot(211)
#ax.set_xlim(-OFFSET, OFFSET + LEN)
ax.set_xlim(chr_MIN-OFFSET, chr_MAX+OFFSET)
#ax.set_xticks([1]+range(1000,HPV_len+100,1000)+[HPV_len])
#ax.set_ylim(-1,1)
ax.set_ylim(0,1)

### genome region
verts = [
    (chr_MIN, 0.4), # left, bottom
    (chr_MIN, 0.5), # left, top
    (chr_MAX,0.5), # right, top
    (chr_MAX,0.4), # right, bottom
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

### add integration point

POS = sorted([128241377,128231055,128241548,
            128231213,128241370,128230632,128235913
            ])  

y = 0
for pos in POS:
    y += 1
    ax.scatter(pos, 0.05*y, c='red',marker='^',edgecolors='')

### add gene annotation
MYC = [(128748315,0.6),(128748315,0.66),(128753680,0.66),(128753680,0.6),(0,0)]
path = Path(MYC, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
#ax.text((105+581)/2.0,-0.25,'E6',horizontalalignment='center',verticalalignment='center',fontsize=6)
PCAT1 = [(128025399,0.6),(128025399,0.66),(128033259,0.66),(128033259,0.6),(0,0)]
path = Path(PCAT1, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)

CCAT1 = [(128219629,0.6),(128219629,0.66),(128231333,0.66),(128231333,0.6),(0,0)]
path = Path(CCAT1, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)

BC106081 = [(128240804,0.7),(128240804,0.76),(128241377,0.76),(128241377,0.7),(0,0)]
path = Path(BC106081, codes)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)

ax.axes.get_yaxis().set_visible(False)
#ax.axes.get_xaxis().set_visible(False)

#################################################
################################################

chr_MIN = 1
chr_MAX= 7857
OFFSET = 100

ax=fig.add_subplot(212)
#ax.set_xlim(-OFFSET, OFFSET + LEN)
ax.set_xlim(chr_MIN-OFFSET, chr_MAX+OFFSET)
#ax.set_xticks([1]+range(1000,HPV_len+100,1000)+[HPV_len])
#ax.set_ylim(-1,1)
ax.set_ylim(0,1)

### genome region
verts = [
    (chr_MIN, 0.5), # left, bottom
    (chr_MIN, 0.6), # left, top
    (chr_MAX,0.6), # right, top
    (chr_MAX,0.5), # right, bottom
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

### add integration point

POS = sorted([929, 23, 2497, 930, 929, 5736, 929])

y = 0
for pos in POS:
    y += 1
    ax.scatter(pos, 0.6+0.05*y, c='red',marker='v',edgecolors='')

## add gene annotation


plt.savefig('HeLa-HPV-Integration-diagram.pdf')


