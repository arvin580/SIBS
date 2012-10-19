#perl pep2dna_5.pl fusion_point_3_2_complete_c_title fusion_point_3_3
#perl pep2dna_5.pl splicing_point_3_2_complete_c_title splicing_point_3_3 


open INFILEa,"$ARGV[1]";
while(<INFILEa>)
{
$adc=0;
$scc=0;
$normal=0;
chomp;
s/\r$//g;
@a=split(/\t/,$_);
for($i=2;$i<@a;$i++)
{
if($a[$i]=~/ADC/)
{
$adc++;
}
if($a[$i]=~/SCC/)
{
$scc++;
}
if($a[$i]=~/Normal/)
{
$normal++;
}
}
$total=$a[1];
$num="$total\t$adc\t$scc\t$normal";
$hash{$a[0]}=$num;
}


open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_symbol";
while($peptide=<INFILE>)
{
$genename=<INFILE>;
chomp($peptide);
chomp($genename);
@a=split(/\:/,$genename);
$peptide=~s/^\#//g;
printf OUTFILE "$a[1]:$a[2]\t$peptide\t$hash{$peptide}\n";
}

