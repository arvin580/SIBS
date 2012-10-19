open INFILE,"peptide";
while(<INFILE>)
{
chomp;
s/\r$//g;
print "*******************************\n";
#$a=`perl find.pl ../FinalDatabase/interception_ipi_reverse_final $_`;
print "$_\n";
$p=`perl find.pl ../FinalDataBase/interception_ipi_reverse_final $_`;
print $p;

if($p && !($p=~/IPI/))
{
@arr=split(/\n/,$p);
$title=$arr[0];
$seq=$arr[1];
@a=split(/\|/,$title);
$fl=$a[5];
$sl=$a[6];
$s=index($seq,$_);
$t=$fl-$s;
$part1=substr($seq,$s,$fl-$s);
$part2=substr($seq,$fl,length($_)-$fl+$s);
#print "*****$part1*****$part2******\n";
$at=$a[0];
$at=~s/^>//g;
if($at)
{
$d=`perl find.pl ../Translate/exon_fusion $at`;
}
print $d;
}
if($d)
{
@dd=split(/\n/,$d);
@att=split(/\:/,$at);
$attt=$att[5];
$s=substr($dd[1],$attt-15,30);
print "$s\n";

if($s)
{
if($o=`perl find2.pl $s`)
{
print "godbless\n";
print $o;
}
else
{
print "pitty\n";
}

}
}
print "*************************************\n\n\n";


}
