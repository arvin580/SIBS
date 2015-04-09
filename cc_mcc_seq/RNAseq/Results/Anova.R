#2013.1.25
#Use Exome data
#Delete genes where no expression was dectected in all eight samples

library(edgeR)
library(DESeq)
library(org.Hs.eg.db)
setwd("I:/[20111101]NGS primary liver cancer/DiffGene/DESeq&edgeR/Data/RawData")
exome<-read.table("I:/[20111101]NGS primary liver cancer/DiffGene/DESeq&edgeR/Data/RawData/all_exome.txt",sep="\t",header=T)


#Design Matrix
#For exome
Tissue <- factor(c(rep("C",8),rep("M",8)))
Cancer<- factor(c("A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B"))
Patient <- factor(c("C10","C10","C4","C4","C5","C5","C9","C9","M10","M10","M5","M5","M6","M6","M7","M7"))
#design.exome<-data.frame(Sample=colnames(exome)[2:17],Tissue=Tissue,Cancer=Cancer)
design.edgeR.anova <- model.matrix(~Cancer + Tissue + Cancer:Tissue, data=ALL)

#not used;Match Ensemble 38640->20771, RNA genes were omitted 
d.exome <- DGEList(counts = exome[,2:17], genes=exome[,1])
idfound <- exome[,1]  %in% mappedRkeys(org.Hs.egENSEMBL)
d.exome <- d.exome[idfound,]
dim(d.exome) 

#Add Entrez GeneID
egENSEMBL <- toTable(org.Hs.egENSEMBL)
m <- match(d.exome$genes[,1], egENSEMBL$ensembl_id)
d.exome$genes$EntrezGene <- egENSEMBL$gene_id[m]
#Add Gene Symbol
egSYMBOL <- toTable(org.Hs.egSYMBOL)
m <- match(d.exome$genes$EntrezGene, egSYMBOL$gene_id)
d.exome$genes$Symbol <- egSYMBOL$symbol[m]

#At most 2% (361) genes have multiple Ensembl Accession,so collapse was omitted
#Normalization
d.exome <- calcNormFactors(d.exome)
d.exome$samples
#Estimate Overall Dispersion
d.exome <- estimateGLMCommonDisp(d.exome, design.edgeR.anova, verbose=TRUE)
#Estimate GeneWise Dispersion
d.exome <- estimateGLMTrendedDisp(d.exome,design.edgeR.anova)
d.exome <- estimateGLMTagwiseDisp(d.exome,design.edgeR.anova)


#Anova by edgeR
design.edgeR.anova <- model.matrix(~Tissue+Cancer+Tissue*Cancer, data=exome)
fit <- glmFit(d.exome, design.edgeR.anova,method='simple')#auto 242 ,linesearch 237 ,levenberg 242,simple 269; 
fit.edgeR.anova <- glmLRT(fit, coef="CancerB:TissueM") 
#fit.edgeR.anova <- glmQLFTest(fit, coef="CancerB:TissueM",abundance.trend=F) #True 53,False 53
edgeR.anova.Degs<-topTags(fit.edgeR.anova,sort.by="p.value",n=dim(exome)[1])$table
dim(subset(edgeR.anova.Degs,FDR<=0.1))

#Anova by DESeq
#exome
exome.deseq<-cbind(d.exome$genes,d.exome$counts)
design.DESeq.anova<-data.frame(Sample=colnames(exome.deseq)[4:19],Tissue=Tissue,Cancer=Cancer)
row.names(design.DESeq.anova)<-design.DESeq.anova[,1];design.DESeq.anova<-design.DESeq.anova[,-1]
Anova.Deseq.Data <- newCountDataSet (cbind(d.exome$genes,d.exome$counts)[,4:19],design.DESeq.anova )
Anova.Deseq.Data <- estimateSizeFactors(Anova.Deseq.Data)
Anova.Deseq.Data <- estimateDispersions(Anova.Deseq.Data,sharingMode='fit-only')
#plotDispEsts( Anova.Deseq.Data )
temp.fit1 = fitNbinomGLMs( Anova.Deseq.Data, count ~ Cancer + Tissue + Cancer:Tissue )
temp.fit0 = fitNbinomGLMs( Anova.Deseq.Data, count ~ Cancer + Tissue)
#str(fit1)
pvals.Anova.Deseq = p.adjust(nbinomGLMTest( temp.fit1, temp.fit0 ),method="BH" )
DESeq.anova.Degs<-cbind(d.exome$genes,cbind(d.exome$counts,pvals.Anova.Deseq))
dim(subset(DESeq.anova.Degs,pvals.Anova.Deseq<=0.1)) #default 458,
intersect(subset(edgeR.anova.Degs,FDR<=0.1)$genes,subset(DESeq.anova.Degs,pvals.Anova.Deseq<=0.1)$genes) #default 79 maximum 79 fit-only 238 gene-est-only 120

write.table(edgeR.anova.Degs,"edgeR.anova.txt",sep="\t")
write.table(DESeq.anova.Degs,"DESeq.anova.txt",sep="\t")

#Get Anova Data
both.anova<-intersect(subset(edgeR.anova.Degs,FDR<=0.1)$genes,subset(DESeq.anova.Degs,pvals.Anova.Deseq<=0.1)$genes)
both.anova.data<-cbind(ICC.DEseq.Degs[match(both.anova,ICC.DEseq.Degs$id),],CHC.DEseq.Degs[match(both.anova,CHC.DEseq.Degs$id),])
both.anova.data<-cbind(edgeR.anova.Degs[match(both.anova,edgeR.anova.Degs$genes),1:3],both.anova.data)
write.table(both.anova.data,"both.anova.data.txt",sep="\t")

