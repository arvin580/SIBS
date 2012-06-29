import re
from PyPlotClass import PyPlot
from PyStatsClass import PyStats
import random

class GenomeSeq :
    def __init__(self) :
        pass
    def quality_pass_012_csv(self,file,sampleNum) :
        import csv
        inFile=open(file)
        ouFile=open(file.rstrip('csv')+'pass012','w')
        csvFile=csv.reader(inFile)
        head=csvFile.next()
        for fields in csvFile :
            if fields[32]=='PASS' :
                for i in range(-sampleNum,0) :
                    if fields[i].find('0/1')==0 or fields[i].find('1/0')==0 :
                        fields[i]='1'
                    elif fields[i].find('1/1')==0 :
                        fields[i]='2'
                    else :
                        fields[i]='0'
                ouFile.write('\t'.join(fields)+'\n')
                            
        inFile.close()
        ouFile.close()
    
    def select_no_synonymous_no_unknown(self,file) :
        inFile=open(file)
        ouFile=open(file+'.nonsynonymous','w')
        for line in inFile :
            line=line.rstrip()
            fields=line.split('\t')
            if fields[2]!='synonymous SNV' and fields[2]!='unknown' :
                ouFile.write(line+'\n')

        inFile.close()
        ouFile.close()


    def multi_calling_split(self,file,samplePosList,sampleNameList) :
        for i,item in enumerate(samplePosList) :
            inFile=open(file)
            ouFile=open(file+'.'+sampleNameList[i],'w')
            for line in inFile :
                line=line.rstrip()
                fields=line.split('\t')
                if int(fields[item])>0 :
                    gene=fields[1]
                    gene=re.split(r'[,;(]',gene)[0]
                    ouFile.write('\t'.join([gene]+fields[21:26]+[fields[item]])+'\n')
            ouFile.close()
            inFile.close()

    def tumor_minus_normal_to_somatic(self,tumorFile,normalFile,oFile) :
        dict_Normal=dict()
        ouFile=open(oFile,'w')
        inFile=open(normalFile)
        dict_Normal=inFile.readlines()
        inFile.close()
        inFile=open(tumorFile)
        for line in inFile :
            if line not in dict_Normal :
                ouFile.write(line)
        ouFile.close()

    def combine_single_somatic(self,iFileList,oFile) :
        dict1=dict()
        for n,file in enumerate(iFileList) :
            inFile=open(file)
            for line in inFile :
                line=line.strip()
                fields=line.split('\t')
                key='\t'.join(fields[0:-1])
                dict1.setdefault(key,[0]*len(iFileList))
                dict1[key][n]=fields[-1]
            inFile.close()
        
        self._sort_dict_by_chrom_postition(dict1,oFile)
    
    def snv_level_to_gene_level(self,iFile,sampleNum) :
        pass
        inFile=open(iFile)
        ouFile=open(iFile+'.gene_level','w')
        dict1=dict()
        list1=list()
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            dict1.setdefault(fields[0],[0]*sampleNum)
            list1.append(fields[0])
            for i,item in enumerate(fields[-sampleNum:]) :
                dict1[fields[0]][i]+=int(item)
        for item in self._uniqueList(list1) :
            ouFile.write(item+'\t'+'\t'.join([str(x) for x in dict1[item]])+'\n')

        inFile.close()
        ouFile.close()

    def gene_two_group_ranksum_test(self,iFile,aList,bList) :
        ps=PyStats()
        ps.ranksum_test_file(iFile,aList,bList)
        
    def gene_two_group_ranksum_test_matshow(self,iFile,geneNum,sampleNameList) :
        geneList=list()
        list1=list()
        row=0
        inFile=open(iFile)
        for line in inFile :
            row+=1
            if row<=geneNum :
                line=line.strip()
                fields=line.split()
                geneList.append(fields[0])
                list1.append([int(x) for x in fields[1:]])
        inFile.close()
        pp=PyPlot()
        pp.heatmap_matshow(list1,sampleNameList,geneList)
        
    def gene_significant_mutated(self,iFile,samplePositionList) :
        total_length=0
        total_num=0
        dict1=dict()
        inFile=open('hg19_max_coding_length')
        for line in inFile :
            line=line.rstrip()
            fields=line.split('\t')
            dict1[fields[0]]=int(fields[1])
        inFile.close()


        inFile=open(iFile)
        for line in inFile :
            line=line.rstrip()
            fields=line.split('\t')
            gn=sum([int(fields[x]) for x in samplePositionList]) 
            gl=dict1[fields[0]]
            if gn >0 :
                total_length+=gl
                total_num+=gn
        inFile.close()
        #print(total_length)
        #print(total_num)

        ps=PyStats()
        inFile=open(iFile)
        ouFile=open(iFile+'.fisher_test','w')
        for line in inFile :
            line=line.rstrip()
            fields=line.split('\t')
            gs=sum([int(fields[x]) for x in samplePositionList]) 
            gl=dict1[fields[0]]
            f=ps.fisher_test([gs,gl,total_num,total_length])
            ouFile.write(str(f)+'\t'+line+'\n')
        inFile.close()
        ouFile.close()
        ps.fdr_adjust_file(iFile+'.fisher_test')



    def _uniqueList(self,inList):
        ouList=list()
        for item in inList :
            if item not in ouList :
                ouList.append(item)
        return ouList


    def _sort_dict_by_chrom_postition(self,aDict,outputfile) :
        '''
        aDict format :key='NOC2L\tchr1\t888659\t888659\tT\tC',val=[1,2,3,4,5]
        '''
        dict1=dict()
        list1=list()
        ouFile=open(outputfile,'w')
        chr=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrM']
        for key in aDict :
            fields=key.split('\t')
            dict1.setdefault(fields[1],[])
            dict1[fields[1]].append(key)
        for key in chr :
            if key in dict1 :
                val=dict1[key]
                val.sort(cmp=lambda x,y:cmp(int(x.split('\t')[2]),int(y.split('\t')[2])))
                list1+=val
        for key in dict1 :
            if key not in chr :
                val=dict1[key]
                val.sort(cmp=lambda x,y:cmp(int(x.split('\t')[2]),int(y.split('\t')[2])))
                list1+=val
        for item in list1 :
            ouFile.write(item+'\t'+'\t'.join([str(x) for x in aDict[item]])+'\n')

        ouFile.close()


    def _make_false_normal_calling_out(self,iFile,ouputFile,somaticNum) :
        #test
        inFile=open(iFile)
        ouFile=open(oFile,'w')
        row=0
        for line in inFile :
            row+=1
        inFile.close()
        L=random.sample(range(1,row+1),row-somaticNum)
        inFile=open(iFile)
        row=0
        for line in inFile :
            row+=1
            if row in L :
                ouFile.write(line)
        ouFile.close()

    def venn_diagram(self,iFile1,iFile2,iFile3=0,setname1='A',setname2='B',setname3='C',filename='test.pdf') :
        pp=PyPlot(filename)
        A=[]
        B=[]
        C=[]
        inFile1=open(iFile1)
        inFile2=open(iFile2)
        for line in inFile1 :
            line=line.strip()
            fields=line.split('\t')
            A.append(fields[0])
        for line in inFile2 :
            line=line.strip()
            fields=line.split('\t')
            B.append(fields[0])
        inFile1.close()
        inFile2.close()
        if iFile3==0 :
            pp.venn_diagram([set(A),set(B)],setname1,setname2)

        else :
            inFile3=open(iFile3)
            for line in inFile3 :
                line=line.strip()
                fields=line.split('\t')
                C.append(fields[0])
            inFile3.close()
            pp.venn_diagram([set(A),set(B),set(C)],setname1,setname2,setname3)


    def _plot_snv_number(self,yList):
        pp=PyPlot()
        pp.single_bar(yList)

