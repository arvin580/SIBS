# perl pep2dna_13.pl fusion_point_3_2_complete_c fusion_point_3_2_complete_c_title_dna fusion_point_3_2_complete_peptide_dna
open INFILE,"$ARGV[1]";
while($line1=<INFILE>)
{
$line2=<INFILE>;
$line3=<INFILE>;
$hash{$line1}="$line2$line3";
}

open INFILEa,"$ARGV[0]";
open OUTFILE,">$ARGV[2]";

while($peptide=<INFILEa>)
{
if($peptide=~/^\#/)
{
$title=<INFILEa>;
if($title=~/^>/)
{
$pepcomplete=<INFILEa>;
printf OUTFILE "$peptide$title$pepcomplete$hash{$peptide}";

}
}
}

