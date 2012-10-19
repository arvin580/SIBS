open INFILE,"peptide_complete_c_title";
open OUTFILE,">peptide_genesymbol";
while($peptide=<INFILE>)
{
$genename=<INFILE>;
chomp($peptide);
chomp($genename);
@a=split(/\:/,$genename);
$peptide=~s/^\#//g;
printf OUTFILE "$a[1]\t$a[2]\t$peptide\n";

}
