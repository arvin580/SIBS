#perl chr_strand.pl fusion_point_3_2_complete_c_title_symbol_unique_pos

open INFILE,"$ARGV[0]";
open OUTFILEa,">$ARGV[0]\_sameChr_sameStr";
open OUTFILEb,">$ARGV[0]\_sameChr_diffStr";
open OUTFILEc,">$ARGV[0]\_diffChr_sameStr";
open OUTFILEd,">$ARGV[0]\_diffChr_diffStr";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
if($a[6] eq $a[9])
{
if($a[8] eq $a[11])
{
printf OUTFILEa "$_\n";
}
else
{
printf OUTFILEb "$_\n";
}

}
else
{
if($a[8] eq $a[11])
{

printf OUTFILEc "$_\n";
}
else
{
printf OUTFILEd "$_\n";
}

}
}
