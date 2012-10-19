open INFILE,"<../Translate/splicing_exon_peptide_qc";
open OUTFILE,">splicing_exon_peptide_qc_digestion";
while($title=<INFILE>)
{
$seq=<INFILE>;
chomp($title);
chomp($seq);
$title=~s/\r$//;
$seq=~s/\r$//;
@tit=split(/\|/,$title);
$point=$tit[2];
$n2=0;
$n1=0;
$n=index($seq,"*");
if($n!=-1)
{
$seq=substr($seq,0,$n);
}
for($i=$point;$i<length($seq);$i++)
{
if($n2<2)
{
if(((substr($seq,$i,1) eq "K")&&(substr($seq,$i+1,1) ne "P"))||((substr($seq,$i,1) eq "R")&&(substr($seq,$i+1,1) ne "P")))
{
$n2++;
}
}
else
{
last;
}
}


for($j=$point-1;$j>=0;$j--)
{
if($n1<2)
{
if(((substr($seq,$j,1) eq "K")&&(substr($seq,$j+1,1) ne "P"))||((substr($seq,$j,1) eq "R")&&(substr($seq,$j+1,1) ne "P")))
{
$n1++;
}
}
else
{
last;
}
}
if($j==-1)
{
$sequence_out=substr($seq,$j+1,$i-$j-1);
$first=$point-$j-1;
$second=$i-$point;
}
else
{
$sequence_out=substr($seq,$j+2,$i-$j-2);
$first=$point-$j-2;
$second=$i-$point;

}
$title_out="$title$first|$second";
if($first>2 && $second>2)
{
printf OUTFILE "$title_out\n";
printf OUTFILE "$sequence_out\n";
}
}
