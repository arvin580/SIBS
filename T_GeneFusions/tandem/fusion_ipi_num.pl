open INFILE,"exon_fusion_ipi_reverse_nosame";
$fusion=0;
$ipi=0;
while(<INFILE>)
{
if(/^>/)
{
if(/IPI/)
{
$ipi++;
}
else
{
$fusion++;
}
}
}
print "$fusion\n$ipi\n";
