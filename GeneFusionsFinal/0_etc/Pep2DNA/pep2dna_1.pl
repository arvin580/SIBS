#perl pep2dna_1.pl fusion_point_3_2 
#perl pep2dna_1.pl splicing_point_3_2 
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_complete";
while($peptide=<INFILE>)
{
printf OUTFILE "#$peptide";
chomp($peptide);
$peptide=~s/\r$//g;
open INFILEa,"../FinalDataBase/fusion_splicing_uniprot_ensembl_contaminated_final";
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
