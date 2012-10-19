open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_only";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
@b=split(/:/,$a[0]);
if($a[-1]==0)
{
$hash{$b[0]}++;
$hash{$b[1]}++;
}
}
while(($key,$val)=each %hash)
{
printf OUTFILE "$key\n";
}
