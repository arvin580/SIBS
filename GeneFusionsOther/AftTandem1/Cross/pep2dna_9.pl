#perl pep2dna_9.pl fusion_point_3_2_complete_c_title2_orig2
open INFILE,"$ARGV[0]";
open OUTFILEa,">$ARGV[0]\_nogap";
open OUTFILEb,">$ARGV[0]\_gap";
while($line1=<INFILE>)
{
$line2=<INFILE>;
$line3=<INFILE>;
$line4=<INFILE>;
$line5=<INFILE>;
if(index($line5,"*",0)==-1)
{
printf OUTFILEa $line1;
printf OUTFILEa $line4;
printf OUTFILEa $line5;
}
else
{
printf OUTFILEb $line1;
printf OUTFILEb $line4;
printf OUTFILEb $line5;
}

}
