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

    def __legacy_tumor_minus_normal_to_somatic(self,tumorFile,normalFile,oFile) :
        ## in list is so slow, cant use
        #dict_Normal=dict()
        ouFile=open(oFile,'w')
        inFile=open(normalFile)
        list_Normal=inFile.readlines()
        inFile.close()
        inFile=open(tumorFile)
        for line in inFile :
            if line not in list_Normal :
                ouFile.write(line)
        ouFile.close()

    def tumor_minus_normal_to_somatic(self,tumorFile,normalFile,oFile) :
        dict_Normal=dict()
        ouFile=open(oFile,'w')
        inFile=open(normalFile)
        #list_Normal=inFile.readlines()
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            k='\t'.join(fields[1:-1])
            dict_Normal[k]=1
        inFile.close()
        #print(len(dict_Normal))

        inFile=open(tumorFile)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            k='\t'.join(fields[1:-1])
            if k not in dict_Normal :
                ouFile.write(line+'\n')

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


    def _make_false_normal_calling_out(self,iFile,oFile,somaticNum) :
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
            #fields=line.split('\t')
            A.append(line)
        for line in inFile2 :
            line=line.strip()
            #fields=line.split('\t')
            B.append(line)
        inFile1.close()
        inFile2.close()
        if iFile3==0 :
            pp.venn_diagram([set(A),set(B)],setname1,setname2)

        else :
            inFile3=open(iFile3)
            for line in inFile3 :
                line=line.strip()
                #fields=line.split('\t')
                C.append(line)
            inFile3.close()
            pp.venn_diagram([set(A),set(B),set(C)],setname1,setname2,setname3)
    
    def __legacy_box_plot(self,iFileList,filename,xLabel=0,yLabel=0) :
        pp=PyPlot(filename)
        aList=[]
        for item in iFileList :
            L=list()
            for it in item :
                row=0
                inFile=open(it)
                for line in inFile :
                    row+=1
                inFile.close()
                L.append(row)
            aList.append(L)
        pp.box_plot(aList,xLabel)

    def box_plot(self,iFile,xLabel) :
        pp=PyPlot()
        inFile=open(iFile)
        head=inFile.readline()
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            pp.filename=iFile+'.'+fields[0]+'.pdf'
            group1=[int(x) for x in fields[-8:-4]]
            group2=[int(x) for x in fields[-4:]]
            pp.box_plot([group1,group2],[xLabel[0]+':'+fields[0],xLabel[1]+':'+fields[0]])


        inFile.close()

    
    def snv_distribution(self,iFile1,iFile2) :
        inFile=open(iFile2)
        dict1=dict()
        dict2=dict()
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            key='\t'.join(fields[21:26])
            dict1[key]=fields[0]+'\t'+fields[2]
        inFile.close()
        
        inFile=open(iFile1)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            key='\t'.join(fields[1:6])
            dict2.setdefault(dict1[key],0)
            dict2[dict1[key]]+=1
        ouFile=open(iFile1+'.dist','w')
        for key in dict2 :
            ouFile.write(key+'\t'+str(dict2[key])+'\n')
        ouFile.close()
    
    def snv_distribution_table(self,iFileList1,iFileList2,oFile) :
        dict1=dict()
        for i in range(len(iFileList1))  :
            sample=iFileList2[i]
            dict1[sample]=dict()
            inFile=open(iFileList1[i])
            for line in inFile :
                line=line.strip()
                fields=line.split('\t')
                key=fields[0]+'\t'+fields[1]
                val=int(fields[2])
                dict1[sample][key]=val
            inFile.close()


            dict1[sample]['StopGain']=dict1[sample].get('exonic;splicing\tstopgain SNV',0)+dict1[sample].get('exonic\tstopgain SNV',0)
            dict1[sample]['StopLoss']=dict1[sample].get('exonic;splicing\tstoploss SNV',0)+dict1[sample].get('exonic\tstoploss SNV',0)
            dict1[sample]['Nonsense']=dict1[sample]['StopGain']+dict1[sample]['StopLoss']

            dict1[sample]['Missense']=dict1[sample].get('exonic\tnonsynonymous SNV',0)+dict1[sample].get('exonic;splicing\tnonsynonymous SNV',0)
            dict1[sample]['Synonymous']=dict1[sample].get('exonic\tsynonymous SNV',0)+dict1[sample].get('exonic;splicing\tsynonymous SNV',0)
            dict1[sample]['UnKnown']=dict1[sample].get('exonic\tunknown',0)+dict1[sample].get('exonic;splicing\tunknown',0)

            dict1[sample]['Coding']=dict1[sample]['Nonsense']+dict1[sample]['Missense']+dict1[sample]['Synonymous']+dict1[sample]['UnKnown']

            dict1[sample]['UTR']=dict1[sample].get('UTR3\t',0)+dict1[sample].get('UTR5\t',0)+dict1[sample].get('UTR5;UTR3\t',0)
            dict1[sample]['ncRNA']=dict1[sample].get('ncRNA_exonic\t',0)+dict1[sample].get('ncRNA_intronic\t',0)+dict1[sample].get('ncRNA_UTR5\t',0)+dict1[sample].get('ncRNA_UTR3\t',0)+dict1[sample].get('ncRNA_UTR5;ncRNA_UTR3\t',0)+dict1[sample].get('ncRNA_splicing\t',0)

            dict1[sample]['NonCoding']=dict1[sample]['UTR']+dict1[sample]['ncRNA']


            dict1[sample]['Splicing']=dict1[sample].get('splicing\t',0)
            dict1[sample]['Other']=dict1[sample].get('intronic\t',0)
            dict1[sample]['Intronic']=dict1[sample]['Splicing']+dict1[sample]['Other']

            dict1[sample]['Intergenic']=dict1[sample].get('intergenic\t',0)+dict1[sample].get('upstream\t',0)+dict1[sample].get('downstream\t',0)+dict1[sample].get('upstream;downstream\t',0)

            dict1[sample]['Genomic']=dict1[sample]['Coding']+dict1[sample]['NonCoding']+dict1[sample]['Intronic']+dict1[sample]['Intergenic']






            type=['Genomic','Coding','Nonsense','StopGain','StopLoss','Missense','Synonymous','UnKnown','NonCoding','UTR','ncRNA','Intronic','Splicing','Other','Intergenic']

        list1=[['']+type]
        for key in iFileList2 :
            L=[key]
            for k in type :
                L.append(str(dict1[key][k]))
            list1.append(L)
                #print(key+'\t'+k+'\t'+str(dict1[key][k]))
        
        ouFile=open(oFile,'w')
        for j in range(len(list1[0])) :
            for i in range(len(list1)) :
                ouFile.write(list1[i][j]+'\t')
            ouFile.write('\n')
    
    def snv_region_based_annotation(self,iFile) :
        inFile=open(iFile)
        dict1=dict()
        head=inFile.readline()
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            dict1[fields[0]]=[int(x) for x in fields[1:]]
        inFile.close()
        pp=PyPlot()
        pp.multi_bar([dict1['Coding'][0:4],dict1['Intronic'][0:4],dict1['NonCoding'][0:4],dict1['Intergenic'][0:4],dict1['Genomic'][0:4]])


    
    def snv_pattern(self,iFileList,xLabel) :
        import numpy as np
        N=len(iFileList)
        dict1=dict()
        for i,item in enumerate(iFileList) :
            inFile=open(item)
            for line in inFile :
                line=line.strip()
                fields=line.split('\t')
                type=fields[4]+fields[5]
                dict1.setdefault(type,[0]*N)
                dict1[type][i]+=1
            inFile.close()

        dict1['T>G/A>C']=list(np.array(dict1['TG'])+np.array(dict1['AC']))
        dict1['T>C/A>G']=list(np.array(dict1['TC'])+np.array(dict1['AG']))
        dict1['T>A/A>T']=list(np.array(dict1['TA'])+np.array(dict1['AT']))
        dict1['C>A/G>T']=list(np.array(dict1['CA'])+np.array(dict1['GT']))
        dict1['C>G/G>C']=list(np.array(dict1['CG'])+np.array(dict1['GC']))
        dict1['C>T/G>A']=list(np.array(dict1['CT'])+np.array(dict1['GA']))


        dict1['SNV']=list(np.array(dict1['T>G/A>C'])+np.array(dict1['T>C/A>G'])+np.array(dict1['T>A/A>T'])+np.array(dict1['C>A/G>T'])+np.array(dict1['C>G/G>C'])+np.array(dict1['C>T/G>A']))

        pp=PyPlot()
        pp.single_bar_multi_bar_vertical_proportion(dict1['SNV'],[dict1['T>G/A>C'],dict1['T>C/A>G'],dict1['T>A/A>T'],dict1['C>A/G>T'],dict1['C>G/G>C'],dict1['C>T/G>A']],xLabel)







    ''' 
    def __dbsnp_classification(self,iFile) :
        ## unfinished
        if iFile.find('dbsnp135')!=-1 :
            inFile=open(iFile)
            ouFile=open(iFile.strip('.txt')+'.single','w')
            for line in inFile :
                line=line.strip()
                fields=line.split('\t')
                if fields[10]=='genomic' and fields[11]=='single' :
                    ouFile.write('\t'.join(fields[1:2]+fields[2:3]+fields[]+fields[]))

            inFile.close()
    '''


    def _plot_snv_number(self,yList):
        pp=PyPlot()
        pp.single_bar(yList)

