#Match CNV and SV
setwd("I:/[20111101]NGS primary liver cancer/DiffGene/DESeq&edgeR/Data/RawData")
snv<-read.table("16s.exome.snv.txt",sep="\t",header=T)
cnv-read.table("CNV.txt",sep="\t",header=T)
sv<-read.table("16s.sv.gene.txt",sep="\t")
virus<-read.table("16s.viruse.gene.txt",sep="\t")

intersect(cnv$Gene,both.data$Symbol) #5
intersect(cnv$Gene,both.anova.data$Symbol) #1
intersect(cnv$Gene,ICC.Specific.data$Symbol) #2
intersect(cnv$Gene,CHC.Specific.data$Symbol) #1

intersect(snv$Gene,both.data$Symbol)
intersect(snv$Gene,both.anova.data$Symbol)
intersect(snv$Gene,ICC.Specific.data$Symbol) #2
intersect(snv$Gene,CHC.Specific.data$Symbol) 

intersect(sv$V1,both.data$Symbol)#14 #15
intersect(sv$V1,both.anova.data$Symbol)#12 ACSL5 
intersect(sv$V1,ICC.Specific.data$Symbol) #20 #19
intersect(sv$V1,CHC.Specific.data$Symbol) #7 #1

intersect(virus$V1,both.data$Symbol)
intersect(virus$V1,both.anova.data$Symbol)
intersect(virus$V1,ICC.Specific.data$Symbol)
intersect(virus$V1,CHC.Specific.data$Symbol)

ICC.Specific.data
CHC.Specific.data
#temp<-intersect(union(temp1,temp2),union(ICC.Specific.data$Symbol,CHC.Specific.data$Symbol))
temp<-intersect(cnv$Gene,both.data$Symbol) #5
cbind(cnv[match(temp,cnv$Gene),],both.data[match(temp,both.data$Symbol),])
temp<-intersect(cnv$Gene,both.anova.data$Symbol)  #1
cbind(cnv[match(temp,cnv$Gene),],both.anova.data[match(temp,both.anova.data$Symbol),])

temp<-intersect(sv$V1,both.data$Symbol)#15 ACSL5 
cbind(sv[match(temp,sv$V1),],both.data[match(temp,both.data$Symbol),])
temp<-intersect(sv$V1,both.anova.data$Symbol)#12 ACSL5 
cbind(sv[match(temp,sv$V1),],both.anova.data[match(temp,both.anova.data$Symbol),])