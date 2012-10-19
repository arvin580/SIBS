open INFILE,"$ARGV[0]";
while($title=<INFILE>)
{
$seq=<INFILE>;
$fs="$ARGV[1]:$ARGV[2]";
$sf="$ARGV[2]:$ARGV[1]";
if($title=~/$fs/||$title=~/$sf/)
{
print $title;
print $seq;
}
}
