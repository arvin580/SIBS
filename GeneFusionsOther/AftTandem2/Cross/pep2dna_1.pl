#perl pep2dna_1.pl fusion_point_3_2 
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_complete";
while($peptide=<INFILE>)
{
printf OUTFILE "#$peptide";
chomp($peptide);
$peptide=~s/\r$//g;
open INFILEa,"/netshare1/home1/people/hansun/GeneFusions/FinalDataBase/fusion_splicing_uniprot_ensemble_contaminated_final";
while($title=<INFILEa>)
{
$seq=<INFILEa>;
if($seq=~/$peptide/)
{
printf OUTFILE $title;
printf OUTFILE $seq;
}
}
}
