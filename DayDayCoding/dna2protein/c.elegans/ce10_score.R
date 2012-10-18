data0=read.delim("chrI.phastCons7way.ce10.wigFix",header=F)
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
write.table(data6,"chrI.phastCons7way.ce10.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrII.phastCons7way.ce10.wigFix",header=F)
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
write.table(data6,"chrII.phastCons7way.ce10.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrIII.phastCons7way.ce10.wigFix",header=F)
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
write.table(data6,"chrIII.phastCons7way.ce10.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrIV.phastCons7way.ce10.wigFix",header=F)
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
write.table(data6,"chrIV.phastCons7way.ce10.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrV.phastCons7way.ce10.wigFix",header=F)
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
write.table(data6,"chrV.phastCons7way.ce10.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrX.phastCons7way.ce10.wigFix",header=F)
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
write.table(data6,"chrX.phastCons7way.ce10.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrM.phastCons7way.ce10.wigFix",header=F)
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
write.table(data6,"chrM.phastCons7way.ce10.all.txt",sep="\t",row.names=F,col.names=F)
