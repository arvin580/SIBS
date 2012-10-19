#open INFILE,"exon_fusion_peptide_qc_digestion_qc_comb_reverse";
open INFILE,"ensemble_protein_comb_reverse";
while($title=<INFILE>)
{
$seq=<INFILE>;
if($title=~/^>annotated/)
{
$n1++;
}

}

print "$n1\n"; 
