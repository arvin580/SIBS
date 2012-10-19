#perl pep2dna_14.pl fusion_point_3_2_complete_peptide_dna

open INFILEa,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_phase";
while($line1=<INFILEa>)
{
$line2=<INFILEa>;
$line3=<INFILEa>;
$line4=<INFILEa>;
$line5=<INFILEa>;

chomp($line1);
chomp($line2);
chomp($line3);
chomp($line4);
chomp($line5);

$line1=~s/\r$//g;
$line2=~s/\r$//g;
$line3=~s/\r$//g;
$line4=~s/\r$//g;
$line5=~s/\r$//g;

@a=split(/\|/,$line2);
$phase1=abs($a[1]);
$phase2=abs($a[3]);
printf OUTFILE "$line1\t$phase1\t$phase2\n";
printf OUTFILE "$line2\n$line3\n$line4\n$line5\n";


}




#open INFILE,"/netshare1/home1/people/hansun/GeneFusions/Translate/CodonUsage";
#my %codon; 
#while(<INFILE>)
#{
#        chomp;  
#        s/\r$//g;
#        @a=split(/\s+/);
#        $codon{$a[0]}=$a[1];
#
#}
#
##$line1="#DGEAGAQGPPGPAGLQER";
##$line2=">genefusions:COL1A1:EMILIN1:ENSE00001739834:ENSE00000732225:54:117|0|18|0|39|18|15&genefusions:COL1A1:EMILIN1:ENSE00001904294:ENSE00000732225:54:117|0|18|0|39|18|15";
##$line3="GPAGKDGEAGAQGPPGPAGLQERLGPQGLLGCR";
##$line4=">genefusions:COL1A1:EMILIN1:ENSE00001739834:ENSE00000732225:54:117";
##$line5="GGTCCTGCTGGCAAAGATGGAGAGGCTGGAGCTCAGGGACCCCCTGGCCCTGCTGGCCTGCAGGAGAGGCTGGGCCCCCAGGGCCTCCTGGGCTGCAGGGACCCCCAGGCCCTGCTGGACCTCCAGGATCACCAGGCAAGGACGGGCAAGAGGGCCCCATCGGGCCACCAG";
#
#open INFILEa,"$ARGV[0]";
#open OUTFILE,">$ARGV[0]\_phase";
#while($line1=<INFILEa>)
#{
#$line2=<INFILEa>;
#$line3=<INFILEa>;
#$line4=<INFILEa>;
#$line5=<INFILEa>;
#
#chomp($line1);
#chomp($line2);
#chomp($line3);
#chomp($line4);
#chomp($line5);
#
#$line1=~s/\r$//g;
#$line2=~s/\r$//g;
#$line3=~s/\r$//g;
#$line4=~s/\r$//g;
#$line5=~s/\r$//g;
#
#
#@l2=split(/\|/,$line2);
#$pep_n1=$l2[-2];
#$pep_n2=$l2[-1];
#
#$pep_s1=substr($line3,0,$pep_n1-1);
#$pep_s2=substr($line3,$pep_n1,$pep_n2);
#
#
#@l4=split(/:/,$line4);
#$dna_n1=$l4[-2];
#$dna_n2=$l4[-1];
#
#$dna_s1=substr($line5,0,$dna_n1);
#$dna_s2=substr($line5,$dna_n1,$dna_n2);
#
#
##print "$pep_n1\n$pep_n2\n$pep_s1\n$pep_s2\n$dna_n1\n$dna_n2\n$dna_s1\n$dna_s2\n";
#
#$n1=0;
#$n2=0;
#
#$peptide=undef;
#for($i=0;$i<=length($dna_s1)-3;$i=$i+3)
#{
#	$three=substr($dna_s1,$i,3);
#	if(exists($codon{$three}))
#	{
#		$peptide.=$codon{$three};
#	}
#	else
#	{
#		$peptide.="?";
#	}
#
#}
#if($peptide=~/$pep_s1/)
#{
#$phase1=0;
#$n1++;
#}
#
#$peptide=undef;
#for($i=0;$i<=length($dna_s2)-3;$i=$i+3)
#{
#	$three=substr($dna_s2,$i,3);
#	if(exists($codon{$three}))
#	{
#		$peptide.=$codon{$three};
#	}
#	else
#	{
#		$peptide.="?";
#	}
#
#}
#if($peptide=~/$pep_s2/)
#{
#$phase2=0;
#$n2++;
#}
#
#$peptide=undef;
#for($i=1;$i<=length($dna_s1)-3;$i=$i+3)
#{
#	$three=substr($dna_s1,$i,3);
#	if(exists($codon{$three}))
#	{
#		$peptide.=$codon{$three};
#	}
#	else
#	{
#		$peptide.="?";
#	}
#
#}
#if($peptide=~/$pep_s1/)
#{
#$phase1=1;
#$n1++;
#}
#
#$peptide=undef;
#for($i=1;$i<=length($dna_s2)-3;$i=$i+3)
#{
#	$three=substr($dna_s2,$i,3);
#	if(exists($codon{$three}))
#	{
#		$peptide.=$codon{$three};
#	}
#	else
#	{
#		$peptide.="?";
#	}
#
#}
#if($peptide=~/$pep_s2/)
#{
#$phase2=1;
#$n2++;
#}
#
#$peptide=undef;
#for($i=2;$i<=length($dna_s1)-3;$i=$i+3)
#{
#	$three=substr($dna_s1,$i,3);
#	if(exists($codon{$three}))
#	{
#		$peptide.=$codon{$three};
#	}
#	else
#	{
#		$peptide.="?";
#	}
#
#}
#if($peptide=~/$pep_s1/)
#{
#$phase1=2;
#$n1++;
#}
#
#$peptide=undef;
#for($i=2;$i<=length($dna_s2)-3;$i=$i+3)
#{
#	$three=substr($dna_s2,$i,3);
#	if(exists($codon{$three}))
#	{
#		$peptide.=$codon{$three};
#	}
#	else
#	{
#		$peptide.="?";
#	}
#
#}
#if($peptide=~/$pep_s2/)
#{
#$phase2=2;
#$n2++;
#}
#
#@b=split(/\|/,$line2);
#
#
#printf OUTFILE "$line1\t$phase1\t$phase2\t$b[1]\t$b[3]\n";
#printf OUTFILE "$line2\n$line3\n$line4\n$line5\n";
#if($n1!=1||$n2!=1)
#{
#print "$line1\t$phase1\t$phase2\n";
#}
#
#}









