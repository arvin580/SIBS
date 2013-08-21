Rcode=r'''
library('Vennerable');
L = list("%s=%s, %s=%s, %s=%s, %s=%s);

plot(v);
dev.off()
'''%('Deletion','c(1,2,3)','Duplication','c(2,3,4)','Inversion','c(2,5)','Translocation','c(2)')
#R=Rscript(Rcode)
print(Rcode)

