data=read.table('human/lncrna_ucsc_human_mrna.fa.seq.len')
human.mrna.len=data[,1]

data=read.table('human/lncrna_ucsc_human_genomic.fa.seq.len')
human.genomic.len=data[,1]

png('human.mrna.seq.len.png')
hist(log2(human.mrna.len))
dev.off()

png('human.genomic.seq.len.png')
hist(log2(human.genomic.len))
dev.off()

##############

data=read.table('mouse/lncrna_ucsc_mouse_mrna.fa.seq.len')
mouse.mrna.len=data[,1]

data=read.table('mouse/lncrna_ucsc_mouse_genomic.fa.seq.len')
mouse.genomic.len=data[,1]

png('mouse.mrna.seq.len.png')
hist(log2(mouse.mrna.len))
dev.off()

png('mouse.genomic.seq.len.png')
hist(log2(mouse.genomic.len))
dev.off()


##############

data=read.table('rat/lncrna_ucsc_rat_mrna.fa.seq.len')
rat.mrna.len=data[,1]

data=read.table('rat/lncrna_ucsc_rat_genomic.fa.seq.len')
rat.genomic.len=data[,1]

png('rat.mrna.seq.len.png')
hist(log2(rat.mrna.len))
dev.off()

png('rat.genomic.seq.len.png')
hist(log2(rat.genomic.len))
dev.off()

