opendir DIR,"$ARGV[0]";
open OUTFILEa,">output_adc_fusionpoint_support";
open OUTFILEb,">output_normal_fusionpoint_support";
open OUTFILEc,">output_scc_fusionpoint_support";
foreach $filename(readdir DIR)
{
open INFILE,"<$ARGV[0]/$filename";
if($filename=~/ADC/)
{
while(<INFILE>)
{
if(/LGPQGLLGCR/)
{
printf OUTFILEa $_;
}


}
}
if($filename=~/Normal/)
{
while(<INFILE>)
{
if(/LGPQGLLGCR/)
{
printf OUTFILEb $_;
}
}
}
if($filename=~/SCC/)
{
while(<INFILE>)
{
if(/LGPQGLLGCR/)
{
printf OUTFILEc $_;
}
}
}
close INFILE;
}
close OUTFILEa;
close OUTFILEb;
close OUTFILEc;

