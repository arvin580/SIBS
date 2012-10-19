#open INFILE,"exon_fusion_peptide_qc_digestion_qc_comb_reverse";
open INFILE,"splicing_exon_peptide_qc_digestion_qc_comb_reverse";
while($title=<INFILE>)
{
$seq=<INFILE>;
if($title=~/^>splicing/)
{
$n1++;
}

}

print "$n1\n"; 
