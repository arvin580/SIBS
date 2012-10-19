open INFILE,"<exon_fusion_peptide_interception";
open OUTFILEa,">exon_fusion_peptide_interception_qc";
open OUTFILEb,">exon_fusion_peptide_interception_qc_gap";
open OUTFILEc,">exon_fusion_peptide_interception_qc_nonKR";
open OUTFILEd,">exon_fusion_peptide_interception_qc_short";
while($title=<INFILE>)
{
$sequence=<INFILE>;
chomp($title);
chomp($sequence);
$title=~s/\r//;
$sequence=~s/\r//;
if($sequence=~/\*/)
{
printf OUTFILEb "$title\n";
printf OUTFILEb "$sequence\n";
}
elsif(!($sequence=~/[KR]/))
{
printf OUTFILEc "$title\n";
printf OUTFILEc "$sequence\n";
}
elsif(length($sequence)<=6)
{
printf OUTFILEd "$title\n";
printf OUTFILEd "$sequence\n";
}
else
{
printf OUTFILEa "$title\n";
printf OUTFILEa "$sequence\n";
}

}
