data=read.table('sum_snp.genome_combined.sorted.pass012.new.pca',row.names=1)
colnames=c('ICC10A','ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A','CHC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A')
colnames(data)=colnames
data.pr=princomp(data,cor=T)
load=loadings(data.pr)
plot(load[,1:2])
text(load[,1],load[,2],adj=c(-0.4,0.3))


