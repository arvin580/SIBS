data0=read.delim("chr2L.pp",header=F)
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
write.table(data6,"chr2L.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chr2LHet.pp",header=F)
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
write.table(data6,"chr2LHet.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chr2R.pp",header=F)
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
write.table(data6,"chr2R.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chr2RHet.pp",header=F)
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
write.table(data6,"chr2RHet.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chr3L.pp",header=F)
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
write.table(data6,"chr3L.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chr3LHet.pp",header=F)
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
write.table(data6,"chr3LHet.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chr3R.pp",header=F)
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
write.table(data6,"chr3R.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chr3RHet.pp",header=F)
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
write.table(data6,"chr3RHet.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chr4.pp",header=F)
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
write.table(data6,"chr4.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrM.pp",header=F)
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
write.table(data6,"chrM.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrU.pp",header=F)
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
write.table(data6,"chrU.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrUextra.pp",header=F)
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
write.table(data6,"chrUextra.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrX.pp",header=F)
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
write.table(data6,"chrX.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrXHet.pp",header=F)
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
write.table(data6,"chrXHet.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)

data0=read.delim("chrYHet.pp",header=F)
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
write.table(data6,"chrYHet.phastCons15way.d.melanogaster.all.txt",sep="\t",row.names=F,col.names=F)
