import matplotlib
#matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 
from RscriptClass  import Rscript
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
            

