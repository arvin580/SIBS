open INFILE,"<$ARGV[0]";
while($title=<INFILE>)
{
$seq=<INFILE>;
if($seq=~/$ARGV[1]/||$title=~/$ARGV[1]/)
{
print $title;
print $seq;
}
}
