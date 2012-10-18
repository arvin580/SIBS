x=c(349,31,23,21,13,10,9,8,5,4,3,2)
y=c(1,1,1,1,1,2,1,1,2,5,6,18)
plot(x,y,type="h",xlab="spectrum number",ylab="peptide number",main="40 peptides & 478 spectrums")


z=read.table("spectrum_matched_peptide")
z=z[,1]
#postscript("spectrum_matched_peptide.eps",width=4, height=3,horizontal=F,onefile=F,paper="special")
postscript("spectrum_matched_peptide.ps")
plot(z,xlab="peptide",ylab="spectrum number",main="558 spectrums matched to 40 peptides",type="o")
dev.off()


z=read.table("spectrum_matched_peptide")
z=z[,1]
pdf("spectrum_matched_peptide.pdf")
plot(z,xlab="peptide",ylab="spectrum number",main="558 spectrums matched to 40 peptides",type="o")
dev.off()


pdf("gene_peptide_num.pdf")
x=read.table("gene_peptide_num")
x=x[,2]
plot(x,xlab="gene",ylab="frequency",type="o")
dev.off()

#used
postscript("gene_pair_name_num.eps",width=8,height=8,horizontal = FALSE, onefile = FALSE, paper = "special")
x=read.table("gene_pair_name_num")
x=x[,2]
plot(x,xlab="gene",ylab="frequency",type="o")
#text(7.5,15,"COL1A1(17q21.33)",col="blue")
#text(7.5,13,"COL1A2(7q22.1)",col="blue")
#text(12,2,"EMILIN1(2p23.3-p23.2)",col="blue")
#text(4,1.5,"SACS(13q12)",col="blue")
dev.off()




data=read.table("fusion_cancer_normal")
adc=data[,1]
scc=data[,2]
normal=data[,3]
pdf("hah")
plot(adc,type="l")
lines(scc,col="green")
lines(normal,col="red")
lines(adc,col="blue")
dev.off()



data=read.table("fusion_cancer_normal")
adc=data[,1]
scc=data[,2]
normal=data[,3]
pdf("fusion_cancer_normal.pdf")
plot(adc,type="p",xlab="fusion peptide",ylab="cancer or normal sample")
points(scc,col="green")
points(normal,col="red")
points(adc,col="blue")
lines(scc,col="green")
lines(normal,col="red")
lines(adc,col="blue")
dev.off()


data=read.table("fusion_cancer_normal")
adc=data[,1]
scc=data[,2]
normal=data[,3]
pdf("fusion_cancer_normal.pdf")
plot(adc,type="n",xlab="fusion peptide",ylab="cancer or normal sample",xlim=c(1,40),ylim=c(1,200))
points(adc,col="blue")
points(scc,col="green")
points(normal,col="red")
lines(adc,col="blue")
lines(scc,col="green")
lines(normal,col="red")
dev.off()


pdf("fusion_cancer_normal.pdf")
data=read.table("fusion_cancer_normal")
adc=data[,1]
scc=data[,2]
normal=data[,3]
plot(adc,type="n",xlab="fusion peptide",ylab="cancer or normal sample",xlim=c(1,40),ylim=c(1,200))
points(normal,col="red")
points(adc,col="blue")
points(scc,col="green")
lines(normal,col="red")
lines(adc,col="blue")
lines(scc,col="green")
legend(32,200,c("adc","scc","normal"),lty=1,col=c("blue","green","red"))
dev.off()


#used
pdf("fusion_cancer_normal.pdf")
data=read.table("fusion_cancer_normal")
data=t(as.matrix(data))
barplot(data,beside=T,ylim=c(0,200),col=c("green","blue","red"),ylab="number of peptides in each kind of sample",xlab="fusion peptides")
legend(120,200,c("adc","scc","normal"),lty=1,col=c("green","blue","red"))
dev.off()

pdf("fusion_cancer_normal2.pdf")
data=read.table("fusion_cancer_normal")
data[,3]=data[,3]/2
data=t(as.matrix(data))
barplot(data,beside=T,ylim=c(0,200),col=c("green","blue","red"),ylab="number of peptides in each kind of sample",xlab="fusion peptides")
legend(120,200,c("adc","scc","normal"),lty=1,col=c("green","blue","red"))
dev.off()

#used
pdf("fusion_cancer_normal.pdf")
par(cex.axis=0.8,mar=c(8,4,4,2))
data=read.table("fusion_cancer_normal")
genepair=read.table("gene_pair_name")
data2=data
data2[,1]=0
data2[,2]=0
data2[,3]=data2[,3]/2
data=t(as.matrix(data))
colnames(data)=genepair[,1]
data2=t(as.matrix(data2))
barplot(data,beside=T,ylim=c(0,200),col=c("green","blue","red"),ylab="number of spectrums in each kind of sample",las=3)
par(new=T)
barplot(data2,beside=T,ylim=c(0,200),col=c("green","blue","yellow"),ylab="",xlab="")
legend(120,200,c("adc","scc","normal","normal/2"),lty=1,col=c("green","blue","red","yellow"))
dev.off()


