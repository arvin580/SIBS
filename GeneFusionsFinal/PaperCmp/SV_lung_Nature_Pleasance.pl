open INFILE,"SV_lung_Nature_Pleasance";
open OUTFILE,">SV_lung_Nature_Pleasance.c";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
$x1=$a[1]-5000;
$x2=$a[1]+5000;
$y1=$a[4]-5000;
$y2=$a[4]+5000;
printf OUTFILE "$a[0]\t$x1\t$x2\t$a[2]\n$a[3]\t$y1\t$y2\t$a[5]\n";
}
