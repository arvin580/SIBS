#perl unique.pl  fusion_point_3_2_complete_c_title_symbol_2
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_unique";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
@b=split(/:/,$a[0]);
$hash{$b[0]}++;
$hash{$b[1]}++;
}
while(($key,$val)=each %hash)
{
printf OUTFILE "$key\n";
}
