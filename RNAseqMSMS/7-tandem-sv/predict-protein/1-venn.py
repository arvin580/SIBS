from Rscript.RscriptClass import Rscript
MSMS = {}
inFile = open('HeLa-Predict-pep.transcript')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    MSMS[fields[0]]=int(fields[1])
inFile.close()

RNASEQ = {}
inFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.splicing.not_known-predict.transcript')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    RNASEQ[fields[0]]=int(fields[1])
inFile.close()

GENSCAN = {}
inFile = open('Homo_sapiens.GRCh37.70.pep.abinitio.fa.fa.transcript')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    GENSCAN[fields[0]]=int(fields[1])
inFile.close()

R=r'''

library(VennDiagram)
venn.plot <- venn.diagram(
 	x = list(
	MS_MS = c('%s'),
 	RNA_Seq = c('%s'),
 	Ensembl_Predict = c('%s')
 		),
 	filename = "Predict-rnaseq-msms-venn.pdf",
 	col = "transparent",
 	fill = c("red", "blue", "green"),
 	alpha = 0.5,
 	label.col = c("darkred", "white", "darkblue", "white", "white", "white", "darkgreen"),
 	cex = 2.5,
 	fontfamily = "serif",
 	fontface = "bold",
 	cat.default.pos = "text",
 	cat.col = c("darkred", "darkblue", "darkgreen"),
 	cat.cex = 2.5,
 	cat.fontfamily = "serif",
 	cat.dist = c(0.06, 0.06, 0.03),
 	cat.pos = 0
 	);

'''%("','".join(MSMS),"','".join(RNASEQ),"','".join(GENSCAN))
Rscript(R)
