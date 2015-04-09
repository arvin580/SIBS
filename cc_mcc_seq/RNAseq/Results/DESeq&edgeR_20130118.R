#For Filtered_AtLeastOneSample
#2013.01.08

library(edgeR)
library(DESeq)
library(org.Hs.eg.db)
setwd("I:/[20111101]NGS primary liver cancer/DiffGene/DESeq&edgeR/Data/Exome_Filtered_AtLeastOneSample")
setwd("/export/home/lyzeng/DiffGene/DESeq/Exome")
load("ICC_MCC.RData")

ICC<-read.table("ICC.txt",sep="\t",header=T)
CHC<-read.table("MCC.txt",sep="\t",header=T)

ICC.DEseq.Degs<-read.table("ICC_DESeq.txt",sep="\t",header=T)
CHC.DEseq.Degs<-read.table("CHC_DESeq.txt",sep="\t",header=T)

#ICC
#Match Ensemble 36016->17857, RNA genes were omitted
d.ICC <- DGEList(counts = ICC[,2:9], genes=ICC[,1])
idfound <- ICC[,1]  %in% mappedRkeys(org.Hs.egENSEMBL)
d.ICC <- d.ICC[idfound,]
dim(d.ICC) 

#Add Entrez GeneID
egENSEMBL <- toTable(org.Hs.egENSEMBL)
head(egENSEMBL)
m <- match(d.ICC$genes[,1], egENSEMBL$ensembl_id)
d.ICC$genes$EntrezGene <- egENSEMBL$gene_id[m]
#Add Gene Symbol
egSYMBOL <- toTable(org.Hs.egSYMBOL)
m <- match(d.ICC$genes$EntrezGene, egSYMBOL$gene_id)
d.ICC$genes$Symbol <- egSYMBOL$symbol[m]

#CHC
#Match Ensemble 35771->17837, RNA genes were omitted
d.CHC <- DGEList(counts = CHC[,2:9], genes=CHC[,1])
idfound <- CHC[,1]  %in% mappedRkeys(org.Hs.egENSEMBL)
d.CHC <- d.CHC[idfound,]
dim(d.CHC) 

#Add Entrez GeneID
egENSEMBL <- toTable(org.Hs.egENSEMBL)
head(egENSEMBL)
m <- match(d.CHC$genes[,1], egENSEMBL$ensembl_id)
d.CHC$genes$EntrezGene <- egENSEMBL$gene_id[m]
#Add Gene Symbol
egSYMBOL <- toTable(org.Hs.egSYMBOL)
m <- match(d.CHC$genes$EntrezGene, egSYMBOL$gene_id)
d.CHC$genes$Symbol <- egSYMBOL$symbol[m]

#At most 2% (427) genes have multiple Ensembl Accession,so collapse was omitted
#Normalization
d.ICC <- calcNormFactors(d.ICC)
d.ICC$samples
d.CHC <- calcNormFactors(d.CHC)
d.CHC$samples

#edgeR
#For ICC Design Matrix
Patient <- factor(c("C10","C10","C4","C4","C5","C5","C9","C9"))
Tissue<- factor(c("A","B","A","B","A","B","A","B"))
data.frame(Sample=colnames(ICC)[2:9],Patient=Patient,Tissue=Tissue)
design.ICC <- model.matrix(~Patient+Tissue)
rownames(design.ICC) <- colnames(ICC)[2:9]
#For CHC Design Matrix
Patient <- factor(c("M10","M10","M5","M5","M6","M6","M7","M7"))
Tissue<- factor(c("A","B","A","B","A","B","A","B"))
data.frame(Sample=colnames(CHC)[2:9],Patient=Patient,Tissue=Tissue)
design.CHC <- model.matrix(~Patient+Tissue)
rownames(design.CHC) <- colnames(CHC)[2:9]

#Estimate Overall Dispersion
d.ICC <- estimateGLMCommonDisp(d.ICC, design.ICC, verbose=TRUE)
d.CHC <- estimateGLMCommonDisp(d.CHC, design.CHC, verbose=TRUE)
#Estimate GeneWise Dispersion
d.CHC <- estimateGLMTrendedDisp(d.CHC,design.CHC)
d.ICC <- estimateGLMTrendedDisp(d.ICC,design.ICC)
d.ICC <- estimateGLMTagwiseDisp(d.ICC,design.ICC)
d.CHC <- estimateGLMTagwiseDisp(d.CHC,design.CHC)

#DEGs
fit.ICC <- glmFit(d.ICC, design.ICC) #ICC
ICC.edgeR <- glmLRT(fit.ICC)
ICC.edgeR.Degs<-topTags(ICC.edgeR,sort.by="p.value",n=dim(ICC)[1])$table
#ICC.edgeR$table[order(ICC.edgeR$table$PValue)[1:10],]
#cpm(d.ICC)[o[1:20],]
fit.CHC <- glmFit(d.CHC, design.CHC) #CHC
CHC.edgeR <- glmLRT(fit.CHC )
CHC.edgeR.Degs<-topTags(CHC.edgeR,sort.by="p.value",n=dim(CHC)[1])$table
write.table(ICC.edgeR.Degs,"ICC_edgeR.txt",sep="\t")
write.table(CHC.edgeR.Degs,"CHC_edgeR.txt",sep="\t")

#DEseq ICC 
ICC.Deseq.label<-1:8;ICC.Deseq.label[seq(1,8,2)] <- "A";ICC.Deseq.label[seq(2,8,2)] <- "B"
row.names(d.ICC$counts)<-d.ICC$genes$genes
ICC.Deseq.Data <- newCountDataSet(d.ICC$counts[,1:8], conditions=ICC.Deseq.label)
ICC.Deseq.Data <- estimateSizeFactors(ICC.Deseq.Data)
sizeFactors(ICC.Deseq.Data)
#ICC.Deseq.Data<-counts(ICC.Deseq.Data,normalized=TRUE) #data will be normalized in nbinomTest
ICC.Deseq.Data <- estimateDispersions(ICC.Deseq.Data)
str(fitInfo(ICC.Deseq.Data))
ICC.DEseq.Degs <- nbinomTest(ICC.Deseq.Data,"A","B")
write.table(ICC.DEseq.Degs, file="ICC_DESeq.txt",sep="\t")

#DEseq CHC
CHC.Deseq.label<-1:8;CHC.Deseq.label[seq(1,8,2)] <- "A";CHC.Deseq.label[seq(2,8,2)] <- "B"
row.names(d.CHC$counts)<-d.CHC$genes$genes
CHC.Deseq.Data <- newCountDataSet (d.CHC$counts[,1:8], CHC.Deseq.label)
CHC.Deseq.Data <- estimateSizeFactors(CHC.Deseq.Data)
sizeFactors(CHC.Deseq.Data)
CHC.Deseq.Data <- estimateDispersions(CHC.Deseq.Data)
str(fitInfo(CHC.Deseq.Data))
CHC.DEseq.Degs <- nbinomTest(CHC.Deseq.Data,"A","B")
write.table(CHC.DEseq.Degs, file="CHC_DESeq.txt",sep="\t")
save.image("/export/home/lyzeng/DiffGene/DESeq/Exome/ICC_MCC.RData")


#Get Common DEGs and Tumor Specific DEGs
#read both;ICC_Specific;CHC_Specific from Venn website
#ICC
idfound<-match(ICC.Specific,ICC.edgeR.Degs$genes);temp<-ICC.edgeR.Degs[idfound,];
idfound<-match(ICC.Specific,CHC.edgeR.Degs$genes);ICC.Specific.data<-cbind(temp,CHC.edgeR.Degs[idfound,]);
#CHC
idfound<-match(CHC.Specific,ICC.edgeR.Degs$genes);temp<-ICC.edgeR.Degs[idfound,];
idfound<-match(CHC.Specific,CHC.edgeR.Degs$genes);CHC.Specific.data<-cbind(temp,CHC.edgeR.Degs[idfound,]);
#both
idfound<-match(both,ICC.edgeR.Degs$genes);temp<-ICC.edgeR.Degs[idfound,];
idfound<-match(both,CHC.edgeR.Degs$genes);both.data<-cbind(temp,CHC.edgeR.Degs[idfound,]);
write.table(ICC.Specific.data,"ICC.Specific.data",sep="\t")
write.table(CHC.Specific.data,"CHC.Specific.data",sep="\t")
write.table(both.data,"both.data",sep="\t")


heatmap.data<-both.data[,2:37]
heatmap.data<-ICC_Specific.data[,seq(2,36,2)]
heatmap.data<-CHC_Specific.data[,seq(2,36,2)]
heatmap.data<-rbind(ICC_Specific.data,CHC_Specific.data)[,2:37]
heatmap.data<-rbind(both.data[,2:37],rbind(ICC_Specific.data,CHC_Specific.data)[,2:37])
color.specific.row<-c(rep("red",length(ICC_Specific)),rep("darkorange1",length(CHC_Specific)))
color.specific.col<-c(rep("darkorange1",8),rep("red",10))

#If all common genes were both up/down regulated in ICC/CHC; yes
count=0
for (i in 1:length(both)){
if (both.data[i,4]*both.data[i,12]<0)
{count=count+1}
}


