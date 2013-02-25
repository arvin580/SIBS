import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 
import time

class PyPlot :

    def ___init__(self,filename='pyplot.'+str(time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime()))+'.pdf') :
        self.filename=filename
        #self.colors=['r','g','b','y','c','m','w','k']
    def __init__(self,filename='') :
        if filename :
            self.filename=filename
        else :
            self.filename='pyplot.'+str(time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime()))+'.pdf'
     
    def get_color(self,i,N) :
        #if i <len(self.colors) :
        #    return self.colors[i]
        #else :
        #    return self.colors[-1]
        cm=plt.get_cmap('gist_rainbow')
        return(cm(i/float(N)))
        

    def show(self):
        #plt.show()
        plt.savefig(self.filename)
    
    def plot1(self, yList, xLabel=[]) :
        fig = plt.figure()
        ax=fig.add_subplot(111)
        ax.plot(yList)
        if xLabel:
            ax.set_xticklabels(xLabel)
        self.show()

    def plot1_xLabel(self, yList, xLabel=[],yTitle='') :
        fig = plt.figure()
        ax=fig.add_subplot(111)
        ax.plot(range(1, len(yList) + 1), yList)
        ax.set_xticks(range(len(yList)+2))
        if xLabel:
            ax.set_xticklabels(['']+xLabel+[''])
        if yTitle:
            ax.set_ylabel(yTitle)

        self.show()

    def plot2(self, aList, xLabel=[]) :
        fig = plt.figure()
        ax=fig.add_subplot(111)
        xList=aList[0]
        yList=aList[1]
        ax.plot(xList,yList)
        if xLabel:
            ax.set_xticklabels(xLabel)
        self.show()

    def hist(self,xList) :
        fig = plt.figure()
        ax=fig.add_subplot(111)
        ax.hist(xList)
        self.show()
        
            
    def single_bar(self,yList,xLabel=0,xTitle=0,yTitle=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList)
        xList=np.arange(n)

        width=0.7
        ax.bar(xList,yList,width,color=self.get_color(1,1))
        #ax.bar(xList,yList,width,color=matplotlib.colors.colorConverter.to_rgb('0.3'))
        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,yList.max()*1.1)
        ax.set_xticks(xList+width/2)

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)
        self.show()


    def single_error_bar(self,yList,errList,xLabel=0,xTitle=0,yTitle=0):
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        errList=np.array(errList)
        n=len(yList)
        xList=np.arange(n)

        width=0.7
        ax.bar(xList,yList,width,color=self.get_color(1,1),yerr=errList)
        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,(yList+errList).max()*1.1)
        ax.set_xticks(xList+width/2)

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)
        self.show()

    def multi_bar(self,yList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.9/N

        bar=[]
        for i in range(N) :
            bar.append(ax.bar(xList+i*width,yList[i],width,color=self.get_color(i,N)))


        ax.set_xlim(-0.1,n)
        ax.set_ylim(0,yList.max()*1.1)
        ax.set_xticks(xList+0.9/2)

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        #ax.set_xticklabels(xLabel)
        ax.set_xticklabels(xLabel,rotation='vertical')

        if legTitle==0 :
            legTitle=['type'+str(i) for i in range(1,N+1)]
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=0.97
        if xTitle :
            ax.set_xlabel(xTitle)
        if yTitle :
            ax.set_ylabel(yTitle)


        legBar=[bar[i][0] for i in range(N)]

        ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])

        self.show()

    def multi_bar_star(self,yList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0,starList=[]) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.9/N

        bar=[]
        for i in range(N) :
            bar.append(ax.bar(xList+i*width,yList[i],width,color=self.get_color(i,N)))


        ax.set_xlim(-0.1,n)
        ax.set_ylim(0,yList.max()*1.1)
        ax.set_xticks(xList+0.9/2)

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        #ax.set_xticklabels(xLabel)
        ax.set_xticklabels(xLabel,rotation='vertical')

        if legTitle==0 :
            legTitle=['type'+str(i) for i in range(1,N+1)]
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=0.97
        if xTitle :
            ax.set_xlabel(xTitle)
        if yTitle :
            ax.set_ylabel(yTitle)

        #ax.text(xList+0.9/2,[1000,1000,1000,1000,1000,1000],'***')
        for i in range(len(starList)) :
            if starList[i] :
                ax.text((xList+0.9/2)[i],yList[:,i].max(),starList[i],horizontalalignment='center')

        legBar=[bar[i][0] for i in range(N)]

        ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])

        self.show()

    def multi_bar_vertical(self,yList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.7

        bar=[]
        bar.append(ax.bar(xList,yList[0],width,color=self.get_color(0,N)))
        for i in range(1,N) :
            bar.append(ax.bar(xList,yList[i],width,bottom=sum(yList[0:i]),color=self.get_color(i,N)))

        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,sum(yList[0:]).max()*1.1)
        ax.set_xticks(xList+width/2)

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)


        if legTitle==0 :
            legTitle=['type'+str(i) for i in range(1,N+1)]
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=0.97

        legBar=[bar[i][0] for i in range(N)]

        ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])

        self.show()

    def multi_bar_vertical_sv_number(self,yList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.7

        bar=[]
        bar.append(ax.bar(xList,yList[0],width,color=self.get_color(0,N)))
        for i in range(1,N) :
            bar.append(ax.bar(xList,yList[i],width,bottom=sum(yList[0:i]),color=self.get_color(i,N)))

        ax.set_xlim(-0.3,n)
        #ax.set_ylim(0,sum(yList[0:]).max()*1.1)
        ax.set_xticks(xList+width/2)


        #####ax.set_yticks(range(sum(yList[0:]).max()+2)) 
        ##### used in /netshare1/home1/szzhongxin/proj1/hansun/16sTranslocation/2.paired.num/5.sv.number.py

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)


        if legTitle==0 :
            legTitle=['type'+str(i) for i in range(1,N+1)]
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=0.97

        legBar=[bar[i][0] for i in range(N)]

        ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])

        self.show()

    def multi_bar_vertical_sv_number2(self,yList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()
        #ax=fig.add_subplot(111)
        ax=fig.add_axes([0.2,0.2,0.7,0.7])

        yList=np.array(yList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.7

        bar=[]
        bar.append(ax.bar(xList,yList[0],width,color=self.get_color(0,N)))
        for i in range(1,N) :
            bar.append(ax.bar(xList,yList[i],width,bottom=sum(yList[0:i]),color=self.get_color(i,N)))

        ax.set_xlim(-0.3,n)
        #ax.set_ylim(0,sum(yList[0:]).max()*1.1)
        ax.set_xticks(xList+width/2)

        ax.set_xticklabels(xLabel,rotation='vertical')

        #####ax.set_yticks(range(sum(yList[0:]).max()+2)) 
        ##### used in /netshare1/home1/szzhongxin/proj1/hansun/16sTranslocation/2.paired.num/5.sv.number.py

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)


        if legTitle==0 :
            legTitle=['type'+str(i) for i in range(1,N+1)]
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=0.97

        legBar=[bar[i][0] for i in range(N)]

        ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])

        self.show()


    def multi_bar_vertical_xlabel_vertical(self,yList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.7

        bar=[]
        bar.append(ax.bar(xList,yList[0],width,color=self.get_color(0,N)))
        for i in range(1,N) :
            bar.append(ax.bar(xList,yList[i],width,bottom=sum(yList[0:i]),color=self.get_color(i,N)))

        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,sum(yList[0:]).max()*1.1)
        ax.set_xticks(xList+width/2)

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel,rotation='vertical')


        if legTitle==0 :
            legTitle=['type'+str(i) for i in range(1,N+1)]
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=0.97

        legBar=[bar[i][0] for i in range(N)]

        ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])

        #self.show()
        plt.savefig(self.filename,bbox_inches='tight')


    def multi_bar_vertical_proportion(self,yList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.7

        bar=[]
        bar.append(ax.bar(xList,yList[0]/sum(yList[0:]).astype('float'),width,color=self.get_color(0,N)))
        for i in range(1,N) :
            bar.append(ax.bar(xList,yList[i],width,bottom=sum(yList[0:i])/sum(yList[0:]).astype('float'),color=self.get_color(i,N)))

        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,1)

        ax.set_xticks(xList+width/2)
        ax.set_yticks([0.0,0.2,0.4,0.6,0.8,1.0])
        ax.set_yticklabels(['0%','20%','40%','60%','80%','100%'])

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)



        if legTitle==0 :
            legTitle=['type'+str(i) for i in range(1,N+1)]
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=0.97

        legBar=[bar[i][0] for i in range(N)]

        ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])

        self.show()

    def single_bar_multi_bar_vertical_proportion(self,yList1,yList2,xLabel=0,xTitle=0,yTitle1=0,yTitle2=0,legTitle=0,legX=0,legY=0) :
        bar2=[]
        fig = plt.figure()

        ax=fig.add_subplot(212)

        yList2=np.array(yList2)
        n=len(yList2[0])
        N=len(yList2)

        xList=np.arange(n)

        width=0.7

        bar2.append(ax.bar(xList,yList2[0]/sum(yList2[0:]).astype('float'),width,color=self.get_color(1,N+1)))
        for i in range(1,N) :
            bar2.append(ax.bar(xList,yList2[i]/sum(yList2[0:]).astype('float'),width,bottom=sum(yList2[0:i])/sum(yList2[0:]).astype('float'),color=self.get_color(i+1,N+1)))

        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,1)

        ax.set_xticks(xList+width/2)
        ax.set_yticks([0.0,0.2,0.4,0.6,0.8,1.0])
        ax.set_yticklabels(['0%','20%','40%','60%','80%','100%'])

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)
        if yTitle2==0 :
            yTitle2='SNV(%)'
        ax.set_ylabel(yTitle2)



        #####

        ax=fig.add_subplot(211)
        bar1=[]

        yList1=np.array(yList1)
        n=len(yList1)
        xList=np.arange(n)

        width=0.7
        bar1.append(ax.bar(xList,yList1,width,color=self.get_color(0,N+1)))
        #ax.bar(xList,yList,width,color=matplotlib.colors.colorConverter.to_rgb('0.3'))
        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,yList1.max()*1.1)
        ax.set_xticks(xList+width/2)
        ax.set_xticklabels([])

        if yTitle1==0 :
            yTitle1='Mutations(n)'
            ax.set_ylabel(yTitle1)
 
        if legTitle==0 :
            #legTitle=['type'+str(i) for i in range(1,len(bar1+bar2)+1)]
            legTitle=['T>G/A>C','T>C/A>G','T>A/A>T','C>A/G>T','C>G/G>C','C>T/G>A','SNV']
        if legX==0 :
            legX=0.5
        if legY==0 :
            legY=1.0

        legBar=[]
        #legBar=[bar[i][0] for i in range(len(bar1+bar2))]
        for i in range(len(bar2)) :
            legBar.append(bar2[i][0])
        for i in range(len(bar1)) :
            legBar.append(bar1[i][0])

        #ax.legend(legBar,legTitle,ncol=4,shadow=True,loc='upper right',bbox_to_anchor=[legX,legY],prop={'size':20})
        #ax.legend(legBar,legTitle,ncol=4,shadow=True,loc='lower center',bbox_to_anchor=[legX,legY],prop={'size':13})
        ax.legend(legBar,legTitle,ncol=4,shadow=False,loc='lower center',bbox_to_anchor=[legX,legY],prop={'size':10})
        #ax.legend(legBar,legTitle,ncol=4,shadow=True,loc=[0,yList1.max()*1.1])
        plt.subplots_adjust(hspace=0.07)

        self.show()

    def single_bar_multi_bar_vertical_proportion_ax(self,yList1,yList2,xLabel=0,xTitle=0,yTitle1=0,yTitle2=0,legTitle=0,legX=0,legY=0) :
        bar2=[]
        fig = plt.figure()
        #ax=fig.add_axes([0.05,0.45,0.9,0.4])
        ax=fig.add_axes([0.1,0.1,0.8,0.35])

        yList2=np.array(yList2)
        n=len(yList2[0])
        N=len(yList2)

        xList=np.arange(n)

        width=0.7

        bar2.append(ax.bar(xList,yList2[0]/sum(yList2[0:]).astype('float'),width,color=self.get_color(1,N+1)))
        for i in range(1,N) :
            bar2.append(ax.bar(xList,yList2[i]/sum(yList2[0:]).astype('float'),width,bottom=sum(yList2[0:i])/sum(yList2[0:]).astype('float'),color=self.get_color(i+1,N+1)))

        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,1)

        ax.set_xticks(xList+width/2)
        ax.set_yticks([0.0,0.2,0.4,0.6,0.8,1.0])
        ax.set_yticklabels(['0%','20%','40%','60%','80%','100%'])

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)
        if yTitle2==0 :
            yTitle2='SNV(%)'
        ax.set_ylabel(yTitle2)



        #####

        #ax=fig.add_axes([0.05,0.05,0.9,0.4])
        ax=fig.add_axes([0.1,0.45,0.8,0.35])
        bar1=[]

        yList1=np.array(yList1)
        n=len(yList1)
        xList=np.arange(n)

        width=0.7
        bar1.append(ax.bar(xList,yList1,width,color=self.get_color(0,N+1)))
        #ax.bar(xList,yList,width,color=matplotlib.colors.colorConverter.to_rgb('0.3'))
        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,yList1.max()*1.1)
        ax.set_xticks(xList+width/2)
        ax.set_xticklabels([])

        if yTitle1==0 :
            yTitle1='Mutations(n)'
            ax.set_ylabel(yTitle1)
 
        if legTitle==0 :
            #legTitle=['type'+str(i) for i in range(1,len(bar1+bar2)+1)]
            legTitle=['T>G/A>C','T>C/A>G','T>A/A>T','C>A/G>T','C>G/G>C','C>T/G>A','SNV']
        #if legX==0 :
        #    legX=0.5
        #if legY==0 :
        #    legY=1.0

        legBar=[]
        #legBar=[bar[i][0] for i in range(len(bar1+bar2))]
        for i in range(len(bar2)) :
            legBar.append(bar2[i][0])
        for i in range(len(bar1)) :
            legBar.append(bar1[i][0])

        #ax.legend(legBar,legTitle,ncol=4,shadow=True,loc='upper right',bbox_to_anchor=[legX,legY],prop={'size':20})
        #ax.legend(legBar,legTitle,ncol=4,shadow=True,loc='lower center',bbox_to_anchor=[legX,legY],prop={'size':13})
        #ax = fig.add_axes([0.05,0.85,0.9,0.1])
        ax=fig.add_axes([0.1,0.8,0.8,0.2])
        #ax.legend(legBar,legTitle,ncol=4,shadow=False,loc='lower center',bbox_to_anchor=[legX,legY],prop={'size':10})
        ax.legend(legBar,legTitle,ncol=4,shadow=False,loc='lower left')
        ax.set_xticks([])
        ax.set_yticks([])
       #ax.legend(legBar,legTitle,ncol=4,shadow=True,loc=[0,yList1.max()*1.1])
        ##plt.subplots_adjust(hspace=0.07)
        self.show()


    def multi_bar_multi_bar_vertical_proportion(self,yList1,yList2,xLabel=0,xTitle=0,yTitle1=0,yTitle2=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()

        ax=fig.add_subplot(212)

        yList2=np.array(yList2)
        bar2=[]
        n=len(yList2[0])
        N=len(yList2)
        cn=len(yList2)+len(yList1)
        ci=0

        xList=np.arange(n)

        width=0.7

        bar2.append(ax.bar(xList,yList2[0]/sum(yList2[0:]).astype('float'),width,color=self.get_color(0,cn)))
        for i in range(1,N) :
            ci+=1
            bar2.append(ax.bar(xList,yList2[i]/sum(yList2[0:]).astype('float'),width,bottom=sum(yList2[0:i])/sum(yList2[0:]).astype('float'),color=self.get_color(ci,cn)))

        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,1)

        ax.set_xticks(xList+width/2)
        ax.set_yticks([0.0,0.2,0.4,0.6,0.8,1.0])
        ax.set_yticklabels(['0%','20%','40%','60%','80%','100%'])

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)
        if yTitle2==0 :
            yTitle2='SNV(%)'
        ax.set_ylabel(yTitle2)



        #####

        ax=fig.add_subplot(211)
        bar1=[]
        yList1=np.array(yList1)
        N=len(yList1)
        n=len(yList1[0])
        xList=np.arange(n)
        width=0.7
        bar1.append(ax.bar(xList,yList1[0],width,color=self.get_color(ci,cn)))
        ci+=1
        for i in range(1,N) :
            bar1.append(ax.bar(xList,yList1[i],width,bottom=sum(yList1[0:i]),color=self.get_color(ci,cn)))
            ci+=1

        #ax.bar(xList,yList,width,color=matplotlib.colors.colorConverter.to_rgb('0.3'))
        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,yList1.max()*1.1)
        ax.set_xticks(xList+width/2)
        ax.set_xticklabels([])

        if yTitle1==0 :
            yTitle1='Mutations(n)'
            ax.set_ylabel(yTitle1)
 
        if legTitle==0 :
            #legTitle=['type'+str(i) for i in range(1,len(bar1+bar2)+1)]
            legTitle=['SNV','INDEL','T>G/A>C','T>C/A>G','T>A/A>T','C>A/G>T','C>G/G>C','C>T/G>A']
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=1.2

        legBar=[]
        #legBar=[bar[i][0] for i in range(len(bar1+bar2))]
        for i in range(len(bar1)) :
            legBar.append(bar1[i][0])
        for i in range(len(bar2)) :
            legBar.append(bar2[i][0])

        ax.legend(legBar,legTitle,ncol=4,shadow=True,loc='upper right',bbox_to_anchor=[legX,legY])
        plt.subplots_adjust(hspace=0.07)

        self.show()



    def single_bar_multi_bar_vertical_sv(self,yList1,yList2,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        C = 5
        fig = plt.figure()
        #ax=fig.add_subplot(211)
        ax=fig.add_axes([0.1,0.57,0.7,0.38])

        yList1=np.array(yList1)
        n=len(yList1)
        xList=np.arange(n)

        width=0.7
        ax.bar(xList,yList1,width,color=self.get_color(0,C))
        #ax.bar(xList,yList,width,color=matplotlib.colors.colorConverter.to_rgb('0.3'))
        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,yList1.max()*1.1)
        ax.set_xticks(xList+width/2)
        ax.set_xticklabels([])

        #ax=fig.add_subplot(212)
        ax=fig.add_axes([0.1,0.15,0.7,0.38])

        yList2=np.array(yList2)
        n=len(yList2[0])
        N=len(yList2)

        xList=np.arange(n)

        width=0.7

        bar=[]
        bar.append(ax.bar(xList,yList2[0],width,color=self.get_color(1,C)))
        for i in range(1,N) :
            bar.append(ax.bar(xList,yList2[i],width,bottom=sum(yList2[0:i]),color=self.get_color(i+1,C)))
        ax.set_xlim(-0.3,n)
        #ax.set_ylim(0,1)

        ax.set_xticks(xList+width/2)
        ax.set_xticklabels(xLabel,rotation='vertical')
        #ax.set_yticks([0.0,0.2,0.4,0.6,0.8,1.0])
        #ax.set_yticklabels(['0%','20%','40%','60%','80%','100%'])

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)

        '''

        if legTitle==0 :
            legTitle=['type'+str(i) for i in range(1,N+1)]
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=0.97

        legBar=[bar[i][0] for i in range(N)]

        ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])
        '''

        self.show()




    def multi_error_bar(self,yList,errList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        errList=np.array(errList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.9/N

        bar=[]
        for i in range(N) :
            bar.append(ax.bar(xList+i*width,yList[i],width,color=self.get_color(i,N),yerr=errList[i]))


        ax.set_xlim(-0.1,n)
        ax.set_ylim(0,(yList+errList).max()+1)
        ax.set_xticks(xList+0.9/2)

        if xLabel==0 :
            xLabel=['bar'+str(i) for i in range(1,n+1)]
        ax.set_xticklabels(xLabel)

        if legTitle==0 :
            legTitle=['type'+str(i) for i in range(1,N+1)]
        if legX==0 :
            legX=0.97
        if legY==0 :
            legY=0.97

        legBar=[bar[i][0] for i in range(N)]

        ax.legend(legBar,legTitle,loc='upper right',bbox_to_anchor=[legX,legY])

        self.show()

    def matshow(self,aList,xLabel=0,yLabel=0) :
        fig = plt.figure()
        plt.grid(True)
        ax=fig.add_subplot(111)
        aList=np.array(aList)

        n=len(aList[0])
        N=len(aList)

        if xLabel==0 :
            xLabel=['s'+str(i) for i in range(1,n+1)]

        if yLabel==0 :
            yLabel=['g'+str(i) for i in range(1,N+1)]

        cax=ax.matshow(aList,cmap=plt.cm.bone_r)
        #cax=ax.matshow(aList,cmap=plt.cm.Greens)

        ax.set_xticks(range(n))
        ax.set_yticks(range(N))

        ax.set_xticklabels(xLabel,rotation='vertical')
        ax.set_yticklabels(yLabel)

        fig.colorbar(cax,ticks=range(aList.max()+1))
        #self.show()
        plt.savefig(self.filename,bbox_inches='tight')

    def heatmap(self,aList,row=True,col=True,xLabel=0,yLabel=0,figsize=0,xLabelVertical=False,grid=False,labelFontSize=False, colorTickets= False) :
        from PyHeatmapClass import PyHeatmap
        ph = PyHeatmap(self.filename)
        #ph.readFile('ppg2008.csv.txt')
        #ph.readFile('test')
        ph.readData(aList, xLabel, yLabel)
        #ph.printData()
        if figsize:
            ph.heatmap(row=row,col=col,figsize=figsize,xLabelVertical=xLabelVertical,grid=grid,labelFontSize=labelFontSize, colorTickets=colorTickets)
        else:
            ph.heatmap(row=row,col=col,xLabelVertical=xLabelVertical,grid=grid,labelFontSize=labelFontSize, colorTickets=colorTickets)

     
    def box_plot(self,aList,xLabel=0,yLabel=0) :
        fig=plt.figure()
        ax=fig.add_subplot(111)
        N=len(aList)
        ax.boxplot(aList)
        if xLabel==0 :
            xLabel=['s'+str(i) for i in range(1,N+1)]
        ax.set_xticklabels(xLabel)
        ax.set_ylim(0,np.array(aList).max()*1.1)
        self.show()

    def venn_diagram(self,aList,setname1='A',setname2='B',setname3='C') :
        from RscriptClass  import Rscript
        N=len(aList)
        if N==2 :
            A=set(aList[0])
            B=set(aList[1])

            AB=len(A&B)
            A_B=len(A-B)
            B_A=len(B-A)

            Rcode=r'''
            library('Vennerable');
            v=Venn(SetNames= c("%s","%s"), Weight=c(%f,%f,%f,%f)); 
            pdf("%s");
            plot(v);
            dev.off()
            '''%(setname1,setname2,0,A_B,B_A,AB,self.filename)
            R=Rscript(Rcode)

        if N==3 :
            A=set(aList[0])
            B=set(aList[1])
            C=set(aList[2])
          
            ABC=len(A&B&C)
            A_B_C=len(A-B-C)
            B_A_C=len(B-A-C)
            C_A_B=len(C-A-B)
            AB_ABC=len(A&B-A&B&C)
            AC_ABC=len(A&C-A&B&C)
            BC_ABC=len(B&C-A&B&C)

            Rcode=r'''
            library('Vennerable');
            v=Venn(SetNames= c("%s","%s","%s"), Weight=c(%f,%f,%f,%f,%f,%f,%f,%f)); 
            pdf("%s");
            plot(v);
            dev.off()
            '''%(setname1,setname2,setname3,0,A_B_C,C_A_B,AC_ABC,B_A_C,AB_ABC,BC_ABC,ABC,self.filename)
            R=Rscript(Rcode)
            

