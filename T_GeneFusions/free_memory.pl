open INFILE,"exon_fusion_peptide";
$n=0;
while(<INFILE>)
{
$a[$n++]=$_;
}
close(INFILE);
