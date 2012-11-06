import matplotlib
#matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.cluster.hierarchy as sch
import time


class PyHeatmap():

    def __init__(self,filename='') :
        if filename :
            self.filename=filename
        else :
            self.filename='pyplot.'+str(time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime()))+'.pdf'
        self.data = []
        self.rowname = []
        self.colname = []
 

    def readFile(self, inF, header=True):
        if inF.find('.csv') != -1:
            sep=','
        else:
            sep='\t'
        data = []
        rowname = []
        colname = []
        if header:
            inFile = open(inF)
            row = 0
            for line in inFile:
                line = line.strip()
                fields = line.split(sep)
                row += 1
                if row == 1:
                    colname = fields[1:]
                else:
                    data.append([float(x) for x in fields[1:]])
                    rowname.append(fields[0])
            inFile.close()
        else:
            inFile = open(inF)
            for line in inFile:
                line = line.strip()
                fields = line.split('\t')
                data.append([float(x) for x in fields])
            inFile.close()
            rowname = ['g' + str(x) for x in range(1,len(data)+1)]
            colname = ['s' + str(x) for x in range(1,len(data[0])+1)]
        self.data = np.array(data)
        self.rowname=np.array(rowname)
        self.colname=np.array(colname)
    
    def readData(self, aList, colname=[], rowname=[]):
        if not rowname :
            rowname = ['g' + str(x) for x in range(1,len(aList)+1)]
        if not colname :
            colname = ['s' + str(x) for x in range(1,len(aList[0])+1)]
        self.data=np.array(aList)
        self.rowname=np.array(rowname)
        self.colname=np.array(colname)

    def printData(self):
        print('data:')
        for x in self.data:
            for y in x:
                print(str(y) + '\t'),
            print('\n'),
        print('row name:')
        print('\t'.join(self.rowname))
        print('column name:')
        print('\t'.join(self.colname))
    
    def stadand(self):
        pass

    def rowDendrogram(self, ax):
        d = sch.distance.pdist(self.data)
        rl = sch.linkage(d, method='complete')
        rd = sch.dendrogram(rl, orientation='right')
        ax.set_xticks([])
        ax.set_yticks([])
        index = rd['leaves']
        self.data = self.data[index,:]
        print(index)
        #self.rowname = self.rowname[index[::-1]]
        self.rowname = self.rowname[index]


    def colDendrogram(self, ax):
        d = sch.distance.pdist(self.data.transpose())
        cl = sch.linkage(d, method='complete')
        cd = sch.dendrogram(cl, orientation='top')
        ax.set_xticks([])
        ax.set_yticks([])
        index = cd['leaves']
        self.data = self.data[:,index]
        self.colname = self.colname[index]

    def showDataName(self, ax, color):
        ax.matshow(self.data, cmap=color, aspect='auto', origin='lower')
        ax.set_xticks(range(len(self.colname)))
        ax.set_yticks(range(len(self.rowname)))
        ax.yaxis.tick_right()
        ax.xaxis.tick_bottom()
        ax.set_xticklabels(self.colname)
        #for label in ax.xaxis.get_ticklabels():
        #        label.set_rotation(90)
        ax.set_yticklabels(self.rowname)
        print(self.rowname)
    
    def showDataColor(self, ax, color, fig):
        colors = [('white')] + [(color(i)) for i in xrange(1,256)]
        new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)
        axm = ax.matshow(self.data, cmap=new_map, aspect='auto', origin='lower')
        plt.grid(True)
        ax.set_xticks(range(len(self.colname)))
        ax.xaxis.tick_bottom()
        ax.set_xticklabels(self.colname)
        ax.set_xticklabels(self.colname, rotation='vertical')
        axcolor = fig.add_axes([0.91,0.1,0.02,0.7])
        plt.colorbar(axm, cax=axcolor)
        #print(self.rowname)
 
    def showDataNameColor(self, ax, color, fig, xLabelVertical,grid,labelFontSize, colorTickets):
        #norm=matplotlib.colors.Normalize(-self.data.max()/2,self.data.max()/2)
        colors = [('white')] + [(color(i)) for i in xrange(1,256)]
        new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)
        axm = ax.matshow(self.data, cmap=new_map, aspect='auto', origin='lower')
        if grid:
            plt.grid(True)
        ax.set_xticks(range(len(self.colname)))
        ax.set_yticks(range(len(self.rowname)))
        ax.yaxis.tick_right()
        ax.xaxis.tick_bottom()
        if xLabelVertical:
            ax.set_xticklabels(self.colname, rotation='vertical')
        else:
            ax.set_xticklabels(self.colname)
        ax.set_yticklabels(self.rowname)
        axcolor = fig.add_axes([0.2,0.03,0.7,0.02])
        if colorTickets:
            x=plt.colorbar(axm, cax=axcolor, orientation='horizontal', ticks=range(self.data.max()+1))
            x.set_label('log value')
        else:
            plt.colorbar(axm, cax=axcolor, orientation='horizontal', ticks=range(self.data.max()+1))
        #cn=['USP6','NCOR1']
        if labelFontSize:
            for t in  ax.yaxis.get_ticklabels() :
            #if t.get_text() in cn :
                t.set_fontsize(labelFontSize)
            #t.set_weight('bold')

 
    def heatmap(self, row=True,col=True,color=plt.cm.jet,figsize=(8,6),xLabelVertical=False,grid=False,labelFontSize=False, colorTickets=False):
        fig = plt.figure(figsize=figsize)
        if row == True and col == True:
            ax = fig.add_axes([0,0.1,0.2,0.7])
            self.rowDendrogram(ax)
            ax = fig.add_axes([0.2,0.8,0.7,0.2])
            self.colDendrogram(ax)
            ax = fig.add_axes([0.2,0.1,0.7,0.7])
            self.showDataNameColor(ax, color, fig,xLabelVertical, grid,labelFontSize)
            self.show()
        if row == True and col == False and xLabelVertical == False:
            ax = fig.add_axes([0,0.1,0.2,0.9])
            self.rowDendrogram(ax)
            ax = fig.add_axes([0.2,0.1,0.7,0.9])
            self.showDataNameColor(ax, color, fig,xLabelVertical,grid,labelFontSize)
            self.show()
        if row == False and col == False:
            ax = fig.add_axes([0.2,0.1,0.7,0.7])
            #self.showDataNameColor(ax, color, fig,xLabelVertical,grid,labelFontSize)
            self.showDataColor(ax, color, fig)
            self.show()
        if row == True and col == False and xLabelVertical == True:
            ax = fig.add_axes([0,0.2,0.2,0.8])
            self.rowDendrogram(ax)
            ax = fig.add_axes([0.2,0.2,0.7,0.8])
            self.showDataNameColor(ax, color, fig,xLabelVertical,grid,labelFontSize, colorTickets)
            self.show()

    def show(self) :
        plt.savefig(self.filename, bbox_inches='tight')




#ph = PyHeatmap()
#ph.readFile('ppg2008.csv.txt')
#ph.readFile('test')
#ph.readData([[1,2,3,4,5],[5,6,7,8,1],[1,1,2,3,2]])
#ph.printData()
#ph.heatmap()
