from scipy import stats
import numpy as np
from RscriptClass import *

class PyStats :
    def __init__(self)  :
        pass
    
    def t_test(self,aList,bList) :
        tt=stats.ttest_ind(aList,bList)
        return tt[1]

    def t_test_file(self,iFile,aList,bList):
        list1=list()
        inFile=open(iFile)
        ouFile=open(iFile+'.t_test','w')
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            a=[]
            b=[]
            for item in aList :
                a.append(fields[item])
            for item in bList :
                b.append(fields[item])
            c=self.t_test(a,b)
            list1.append(str(c)+'\t'+line)
        inFile.close()

        list1.sort(cmp=lambda x,y:cmp(float(x.split('\t')[0]),float(y.split('\t')[0])))
        for item in list1 :
            ouFile.write(item+'\n')
                    
        ouFile.close()
    
    def fisher_test(self,aList) :
        fisher=stats.fisher_exact([[aList[0],aList[1]],[aList[2],aList[3]]])
        return fisher[1]

    def fdr_adjust_file(self,iFile) :
        Rcode=r'''
        data=read.table('%s')
        data=as.matrix(data)
        p=data[,1]
        fdr=p.adjust(p,'fdr',length(p))
        out=cbind(fdr,data)
        write.table(out,'%s',quote=F,sep='\t',row.names=F,col.names=F)
        '''%(iFile,iFile+'.fdr')
        Rscript(Rcode)

        

    def ranksum_test(self,aList,bList) :
        rt=stats.ranksums(aList,bList)
        return rt[1]

    def ranksum_test_file(self,iFile,aList,bList):
        inFile=open(iFile)
        ouFile=open(iFile+'.ranksum_test','w')
        list1=list()
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            a=[]
            b=[]
            for item in aList :
                a.append(fields[item])
            for item in bList :
                b.append(fields[item])
            c=self.ranksum_test(a,b)
            list1.append(str(c)+'\t'+line)

        list1.sort(cmp=lambda x,y:cmp(float(x.split('\t')[0]),float(y.split('\t')[0])))
        for item in list1 :
            ouFile.write(item+'\n')
        ouFile.close()

