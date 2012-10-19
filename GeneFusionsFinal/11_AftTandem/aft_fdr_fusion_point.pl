#perl  aft_fdr_fusion_point.pl FDR_fusions fusion_point_3 3
#perl  aft_fdr_fusion_point.pl FDR_splicing splicing_point_3 3
opendir DIR,"$ARGV[0]";
open OUTFILE,">$ARGV[1]";
foreach $filename(readdir DIR)
{
open INFILE,"<$ARGV[0]/$filename";
while(<INFILE>)
{
@line=split(/\t/,$_);
@fusion=split(/\+/,$line[2]);
@exon=split(/\|/,$fusion[0]);
$point=$exon[5];
$start=$line[5];
$end=$line[6];
if(($point-$start+1)>=$ARGV[2] && ($end-$point)>=$ARGV[2])
{
printf OUTFILE $_;
}
}
close INFILE;
}
close OUTFILE;
