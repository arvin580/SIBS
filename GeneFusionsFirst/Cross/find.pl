open INFILE,"$ARGV[0]";
while($title=<INFILE>)
{
$seq=<INFILE>;
if($title=~/$ARGV[1]/)
{
print $title;
print $seq;
}
}
