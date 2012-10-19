open INFILE,"peptide_complete_c_title";
while($peptide=<INFILE>)
{
$name=<INFILE>;
chomp($peptide);
$peptide=~s/\r$//g;
$peptide=~s/^\#//g;
@a=split(/\:/,$name);
$hash{$peptide}="$a[1]:$a[2]";
}

open INFILEa,"fusion_cancer_normal";
open OUTFILE,">fusion_cancer_normal_genename";
while(<INFILEa>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
if(exists($hash{$a[0]}))
{
printf OUTFILE "$hash{$a[0]}\t$_\n";
}
else
{
print "$a[0]\n";
}
}
