#perl unique.pl fusion_point_3_2_complete_c_title_symbol
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_unique";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
if(!exists($hash{$a[0]}))
{
$hash{"$a[0]"}=$_;
}
}
while(($key,$val)=each %hash)
{
printf OUTFILE "$val\n";
}
