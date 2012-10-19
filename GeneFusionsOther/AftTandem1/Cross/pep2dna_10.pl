#perl pep2dna_10.pl fusion_point_3_2_complete_c_title2_orig2_nogap
#perl pep2dna_10.pl fusion_point_3_2_complete_c_title2_orig2_gap

open INFILE,"fusion_point_3_2_complete_c_title_symbol";
while(<INFILE>)
{
chomp;
s/\r$//g;
@s=split(/\t/,$_);
$hash{$s[1]}="$s[3]\t$s[4]\t$s[5]";
}




open INFILEa,"$ARGV[0]";
open OUTFILEa,">$ARGV[0]\_noshort";
open OUTFILEb,">$ARGV[0]\_short";
while($line1=<INFILEa>)
{
$line2=<INFILEa>;
$line3=<INFILEa>;
chomp($line1);
chomp($line2);
chomp($line3);
$line1=~s/\r$//g;
$line1=~s/^#//g;
$line2=~s/\r$//g;
$line3=~s/\r$//g;
@a=split(/\|/,$line2);
if($a[2]>=15 && $a[4]>=15)
{

$line3_15=substr($line3,$a[2]-15,30);
printf OUTFILEa "$line3_15\t";
printf OUTFILEa "$line1\t";
printf OUTFILEa "$line2\t";
printf OUTFILEa "$line3\t";
printf OUTFILEa "$hash{$line1}\n";

}
else
{
if($a[2]<15)
{
$line3_15=substr($line3,0,$a[2]+15);
printf OUTFILEb "$line3_15\t";
printf OUTFILEb "$line1\t";
printf OUTFILEb "$line2\t";
printf OUTFILEb "$line3\t";
printf OUTFILEb "$hash{$line1}\n";



}
elsif($a[4]<15)
{
$line3_15=substr($line3,$a[2]-15,$a[4]+15);
printf OUTFILEb "$line3_15\t";
printf OUTFILEb "$line1\t";
printf OUTFILEb "$line2\t";
printf OUTFILEb "$line3\t";
printf OUTFILEb "$hash{$line1}\n";


}
else
{
$line3_15=$line3;
printf OUTFILEb "$line3_15\t";
printf OUTFILEb "$line1\t";
printf OUTFILEb "$line2\t";
printf OUTFILEb "$line3\t";
printf OUTFILEb "$hash{$line1}\n";


}

}

}
