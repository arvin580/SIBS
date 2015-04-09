data=read.table("sum_indel.exome_combined.sorted.pass012.new.gene_ttest")

ttest=function(list)
{
x=list[3:12]
y=list[13:22]
xy=t.test(x,y)
return(xy$p.value)
}

for(i in c(1:nrow(data)))
{
if(var(as.numeric(data[i,3:ncol(data)]))!=0)
{
a=ttest(data[i,])
print(a)
}
}
