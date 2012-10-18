#########used##############
pdf("fusion_cancer_normal.pdf")
par(cex.axis=0.8,mar=c(8,4,4,2))
x=read.table("fusion_point_3_2_complete_c_title_symbol_3")
genepair=x[,1]
data=x[,4:6]
data2=data
data2[,1]=0
data2[,2]=0
data2[,3]=data2[,3]/2
data=t(as.matrix(data))
colnames(data)=genepair
data2=t(as.matrix(data2))
barplot(data,beside=T,ylim=c(0,200),col=c("green","blue","red"),ylab="number of spectrums in each kind of sample",las=3)
par(new=T)
barplot(data2,beside=T,ylim=c(0,200),col=c("green","blue","yellow"),ylab="",xlab="")
legend(110,200,c("adc","scc","normal","normal/2"),lty=1,col=c("green","blue","red","yellow"))
dev.off()

##########used X10###############
pdf("fusion_cancer_normal.pdf")
par(cex.axis=0.8,mar=c(8,4,4,2))
x=read.table("fusion_point_3_2_complete_c_title_symbol_3")
genepair=x[,1]
data=x[,4:6]
data[1:2,]=data[1:2,]/10
data2=data
data2[,1]=0
data2[,2]=0
data2[,3]=data2[,3]/2
data=t(as.matrix(data))
colnames(data)=genepair
data2=t(as.matrix(data2))
barplot(data,beside=T,ylim=c(0,22),col=c("green","blue","red"),ylab="number of spectrums in each kind of sample",las=3)
par(new=T)
barplot(data2,beside=T,ylim=c(0,22),col=c("green","blue","yellow"),ylab="",xlab="")
legend(110,20,c("adc","scc","normal","normal/2"),lty=1,col=c("green","blue","red","yellow"))
#text(13,20,"(83,89,179)/10")
#text(17,18,"(13,12,193)/10")
text(2.5,18.5,"x10")
text(9,20,"x10")
dev.off()


pdf("fusion_cancer_normal_2.pdf")
par(cex.axis=0.8,mar=c(8,4,4,2))
x=read.table("fusion_point_3_2_complete_c_title_symbol_2")
genepair=x[,1]
data=x[,4:6]
data2=data
data2[,1]=0
data2[,2]=0
data2[,3]=data2[,3]/2
data=t(as.matrix(data))
colnames(data)=genepair
data2=t(as.matrix(data2))
barplot(data,beside=T,ylim=c(0,200),col=c("green","blue","red"),ylab="number of spectrums in each kind of sample",las=3)
par(new=T)
barplot(data2,beside=T,ylim=c(0,200),col=c("green","blue","yellow"),ylab="",xlab="")
legend(120,200,c("adc","scc","normal","normal/2"),lty=1,col=c("green","blue","red","yellow"))
dev.off()

###########used######################
pdf("splicing_cancer_normal.pdf")
par(cex.axis=0.8,mar=c(8,4,4,2))
x=read.table("splicing_point_3_2_complete_c_title_symbol_2")
genepair=x[,1]
data=x[,4:6]
data2=data
data2[,1]=0
data2[,2]=0
data2[,3]=data2[,3]/2
data=t(as.matrix(data))
colnames(data)=genepair
data2=t(as.matrix(data2))
barplot(data,beside=T,ylim=c(0,20),col=c("green","blue","red"),ylab="number of spectrums in each kind of sample",las=3)
par(new=T)
barplot(data2,beside=T,ylim=c(0,20),col=c("green","blue","yellow"),ylab="",xlab="")
legend(45,20,c("adc","scc","normal","normal/2"),lty=1,col=c("green","blue","red","yellow"))
dev.off()


####### used #########
pdf("fusion_gene_num.pdf")
x=read.table("fusion_point_3_2_complete_c_title_symbol_3_num")
x=x[,2]
plot(x,xlab="fusion gene",ylab="gene frequency",type="o")
text(8,8,"COL1A2(7q22.1)",col="blue")
text(10,7,"COL1A1(17q21.33)",col="blue")
text(11,2.3,"MYH9(22q13.1)",col="blue")
text(11,2,"USP6(17p13)",col="blue")
text(14,1.7,"CALM1(14q24-q31)",col="blue")
dev.off()



####### used #########
pdf("splicing_gene_num.pdf")
x=read.table("splicing_point_3_2_complete_c_title_symbol_2_num")
x=x[,2]/2
plot(x,xlab="splicing gene",ylab="gene frequency",type="o")
text(2.8,2,"COL1A2(7q22.1)",col="blue")
dev.off()



#####Chr_Strand##########
pdf("chr_str.pdf")
chimer=c(2920,2694,294,302)
fusion=c(34,17,2,3)
names(chimer)=c("Chr.diff_Strand.diff","Chr.diff_Strand.same","Chr.same_Strand.diff","Chr.same_Strand.same")
names(fusion)=c("Chr.diff_Strand.diff","Chr.diff_Strand.same","Chr.same_Strand.diff","Chr.same_Strand.same")
layout(matrix(c(1,2),2,1))
barplot(chimer,beside=T,col=c("green","blue","red","yellow"),ylab="No. fusions",main="6210 fusions from chimerdb 2.0")
barplot(fusion,beside=T,col=c("green","blue","red","yellow"),ylab="No. fusions",main="56 fusions identified")
dev.off()

#####chr_str used
png("chr_str.png",800,500)
chimer=c(2920,2694,294,302)
fusion=c(34,17,2,3)
names(chimer)=c("Chr.diff_Strand.diff","Chr.diff_Strand.same","Chr.same_Strand.diff","Chr.same_Strand.same")
names(fusion)=c("Chr.diff_Strand.diff","Chr.diff_Strand.same","Chr.same_Strand.diff","Chr.same_Strand.same")
layout(matrix(c(1,2),2,1))
barplot(chimer,beside=T,col=c("green","blue","red","yellow"),ylab="No. fusions",main="6210 fusions from chimerdb 2.0")
barplot(fusion,beside=T,col=c("green","blue","red","yellow"),ylab="No. fusions",main="56 fusions identified")
dev.off()

x=matrix(c(2920,34,6210,56),2,2)
phyper(x[2,1],x[1,1],x[1,2]-x[1,1],x[2,2],lower.tail=F)

x=matrix(c(2694,17,6210,56),2,2)
phyper(x[2,1],x[1,1],x[1,2]-x[1,1],x[2,2],lower.tail=F)

x=matrix(c(294,2,6210,56),2,2)
phyper(x[2,1],x[1,1],x[1,2]-x[1,1],x[2,2],lower.tail=F)

x=matrix(c(302,3,6210,56),2,2)
phyper(x[2,1],x[1,1],x[1,2]-x[1,1],x[2,2],lower.tail=F)
