data0=read.delim("chr14.phastCons46way.wigFix",header=F)
data1=as.character(unlist(data0))

#The position of each unit in the original data
unit=which(is.na(as.numeric(data1)))

#The start position of each unit
FirLoc=c()
for(i in 1:length(unit))
{
 temp1=unlist(strsplit(data1[unit[i]], " "))[3]
 FirLoc[i]=unlist(strsplit(temp1,"="))[2]
}

#The content of each unit
data3=list()  
for(i in 1:length(unit))
{
  if((i+1)<=length(unit))
    data3[i]=list(data1[(unit[i]+1):(unit[i+1]-1)])
  else
     data3[i]=list(data1[(unit[i]+1):length(data1)])
  }

#The position of each site
Fst_End=list()
for(i in 1:length(unit))
 {
   fst=as.integer(FirLoc[i])
   end=fst+length(data3[[i]])-1
   Fst_End[i]=list(c(fst:end))
 }
 
#Convert into a two-dimensional matrix
p=list()
for(i in 1:length(unit))
{
 p[i]=list(cbind(Fst_End[[i]],as.numeric(data3[[i]])))   
}

data4=do.call(rbind, p)
data5=data4[data4[,2]>=0.0,]
colnames(data5)=c("local","score")
data6=as.matrix(data5,ncol=2)
write.table(data6,"chr14.phastCons46way.wigFix.all.txt",sep="\t",row.names=F,col.names=F)

#mapping to protein sequence
#data_2=read.delim("dna_protein_out_chr20",header=F)
#data_3=as.matrix(data_2)
#data_3[,2]=as.numeric(data_3[,2])
#data_4=data_2[data_2[,1]=="chr1",]
#data10=as.matrix(as.numeric(data_3[,2]),1,5494827)
#data11=data.frame(a=data10,data=c(1:5494827))


#DATA=merge(data_3,data5,by.x="V2",by.y="local")
#write.table(DATA,"dna_protein_out_chr20_score.txt",sep="\t",row.names=F,col.names=F)
