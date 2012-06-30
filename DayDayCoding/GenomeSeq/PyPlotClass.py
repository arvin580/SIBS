import matplotlib
#matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 
import time

class PyPlot :

    def __init__(self,filename='pyplot.'+str(time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime()))+'.pdf') :
        self.filename=filename
        self.colors=['r','g','b','y','c','m','w','k']
    
    def get_color(self,i) :
        if i <len(self.colors) :
            return self.colors[i]
        else :
            return self.colors[-1]
        

    def show(self):
        plt.show()
        #plt.savefig(self.filename)
    
    def plot(self,*arg) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        if len(arg)==1 :
            yList=arg[0]
            ax.plot(yList)
            self.show()
        if len(arg)==2 :
            xList=arg[0]
            yList=arg[1]
            ax.plot(xList,yList)
            self.show()
            
    def single_bar(self,yList,xLabel=0,xTitle=0,yTitle=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList)
        xList=np.arange(n)

        width=0.7
        ax.bar(xList,yList,width,color=self.get_color(1))
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
        ax.bar(xList,yList,width,color=self.get_color(1),yerr=errList)
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
            bar.append(ax.bar(xList+i*width,yList[i],width,color=self.get_color(i)))


        ax.set_xlim(-0.1,n)
        ax.set_ylim(0,yList.max()+1)
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

    def multi_bar_vertical(self,yList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.7

        bar=[]
        bar.append(ax.bar(xList,yList[0],width,color=self.get_color(0)))
        for i in range(1,N) :
            bar.append(ax.bar(xList,yList[i],width,bottom=sum(yList[0:i]),color=self.get_color(i)))

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

    def multi_bar_vertical_proportion(self,yList,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)

        yList=np.array(yList)
        n=len(yList[0])
        N=len(yList)

        xList=np.arange(n)

        width=0.7

        bar=[]
        bar.append(ax.bar(xList,yList[0]/sum(yList[0:]).astype('float'),width,color=self.get_color(0)))
        for i in range(1,N) :
            bar.append(ax.bar(xList,yList[i],width,bottom=sum(yList[0:i])/sum(yList[0:]).astype('float'),color=self.get_color(i)))

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

        bar2.append(ax.bar(xList,yList2[0]/sum(yList2[0:]).astype('float'),width,color=self.get_color(0)))
        for i in range(1,N) :
            bar2.append(ax.bar(xList,yList2[i],width,bottom=sum(yList2[0:i])/sum(yList2[0:]).astype('float'),color=self.get_color(i)))

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
        bar1.append(ax.bar(xList,yList1,width,color=self.get_color(7)))
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
            legX=0.97
        if legY==0 :
            legY=0.97

        legBar=[]
        #legBar=[bar[i][0] for i in range(len(bar1+bar2))]
        for i in range(len(bar2)) :
            legBar.append(bar2[i][0])
        for i in range(len(bar1)) :
            legBar.append(bar1[i][0])

        ax.legend(legBar,legTitle,ncol=4,shadow=True,loc='upper right',bbox_to_anchor=[legX,legY])
        plt.subplots_adjust(hspace=0.05)

        self.show()

    def multi_bar_multi_bar_vertical_proportion(self,yList1,yList2,xLabel=0,xTitle=0,yTitle1=0,yTitle2=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()

        ax=fig.add_subplot(212)

        yList2=np.array(yList2)
        bar2=[]
        n=len(yList2[0])
        N=len(yList2)

        xList=np.arange(n)

        width=0.7

        bar2.append(ax.bar(xList,yList2[0]/sum(yList2[0:]).astype('float'),width,color=self.get_color(0)))
        for i in range(1,N) :
            bar2.append(ax.bar(xList,yList2[i],width,bottom=sum(yList2[0:i])/sum(yList2[0:]).astype('float'),color=self.get_color(i)))

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
        #bar1.append(ax.bar(xList,yList1,width,color=self.get_color(7)))
        bar1.append(ax.bar(xList,yList1[0],width,color=self.get_color(0)))
        for i in range(1,N) :
            bar1.append(ax.bar(xList,yList1[i],width,bottom=sum(yList1[0:i]),color=self.get_color(i)))

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
            legY=0.97

        legBar=[]
        #legBar=[bar[i][0] for i in range(len(bar1+bar2))]
        for i in range(len(bar1)) :
            legBar.append(bar1[i][0])
        for i in range(len(bar2)) :
            legBar.append(bar2[i][0])

        ax.legend(legBar,legTitle,ncol=4,shadow=True,loc='upper right',bbox_to_anchor=[legX,legY])
        plt.subplots_adjust(hspace=0.05)

        self.show()



    '''
    def single_bar_multi_bar_vertical_proportion(self,yList1,yList2,xLabel=0,xTitle=0,yTitle=0,legTitle=0,legX=0,legY=0) :
        fig = plt.figure()

        ax=fig.add_subplot(211)

        yList1=np.array(yList1)
        n=len(yList1)
        xList=np.arange(n)

        width=0.7
        ax.bar(xList,yList1,width,color=self.get_color(1))
        #ax.bar(xList,yList,width,color=matplotlib.colors.colorConverter.to_rgb('0.3'))
        ax.set_xlim(-0.3,n)
        ax.set_ylim(0,yList1.max()*1.1)
        ax.set_xticks(xList+width/2)
        ax.set_xticklabels([])

        ax=fig.add_subplot(212)

        yList2=np.array(yList2)
        n=len(yList2[0])
        N=len(yList2)

        xList=np.arange(n)

        width=0.7

        bar=[]
        bar.append(ax.bar(xList,yList2[0]/sum(yList2[0:]).astype('float'),width,color=self.get_color(0)))
        for i in range(1,N) :
            bar.append(ax.bar(xList,yList2[i],width,bottom=sum(yList2[0:i])/sum(yList2[0:]).astype('float'),color=self.get_color(i)))

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

    '''



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
            bar.append(ax.bar(xList+i*width,yList[i],width,color=self.get_color(i),yerr=errList[i]))


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

    def heatmap_matshow(self,aList,xLabel=0,yLabel=0) :
        fig = plt.figure()
        ax=fig.add_subplot(111)
        aList=np.array(aList)

        n=len(aList[0])
        N=len(aList)

        if xLabel==0 :
            xLabel=['s'+str(i) for i in range(1,n+1)]

        if yLabel==0 :
            yLabel=['g'+str(i) for i in range(1,N+1)]

        cax=ax.matshow(aList,cmap=plt.cm.bone_r)

        ax.set_xticks(range(n))
        ax.set_yticks(range(N))

        ax.set_xticklabels(xLabel,rotation='vertical')
        ax.set_yticklabels(yLabel)

        fig.colorbar(cax,ticks=range(aList.max()+1))

        self.show()
        

    def venn_diagram(self,aList,setname1='C',setname2='B',setname3='C') :
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
            

