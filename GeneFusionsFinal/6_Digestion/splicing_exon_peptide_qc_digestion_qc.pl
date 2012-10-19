open INFILE,"<splicing_exon_peptide_qc_digestion";
open OUTFILEa,">splicing_exon_peptide_qc_digestion_qc";
#open OUTFILEb,">exon_fusion_peptide_qc_digestion_qc_gap";
#open OUTFILEc,">exon_fusion_peptide_digestion_qc_nonKR";
#open OUTFILEd,">exon_fusion_peptide_qc_digestion_qc_short";
while($title=<INFILE>)
{
$sequence=<INFILE>;
chomp($title);
chomp($sequence);
$title=~s/\r//;
$sequence=~s/\r//;
#if($sequence=~/\*/)
#{
#printf OUTFILEb "$title\n";
#printf OUTFILEb "$sequence\n";
#}
#elsif(!($sequence=~/[KR]/))
#{
#printf OUTFILEc "$title\n";
#printf OUTFILEc "$sequence\n";
#}
if(length($sequence)>=6)
{
printf OUTFILEa "$title\n";
printf OUTFILEa "$sequence\n";
}

}
