#perl frameshift.pl fusion_point_3_2_complete_c_title2_orig2_gap_noshort_c

open INFILE,"/netshare1/home1/people/hansun/GeneFusions/Ensemble/exon_phase";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
$hash{$a[2]}=$a[-1];
}
close INFILE;


open INFILEa,"fusion_point_3_2_complete_c_title2_orig2_nogap_noshort_c";
open OUTFILE,">fusion_point_3_2_complete_c_title2_orig2_nogap_noshort_c_phase";
while(<INFILEa>)
{
@a=split(/\t/,$_);
@b=split(/:/,$a[2]);
$phase1=$hash{$b[3]};
$phase2=$hash{$b[4]};

@c=split(/\|/,$a[2]);
$ph1=(3-abs($c[1]))%3;
$ph2=(3-abs($c[3]))%3;


printf OUTFILE "$ph1\t$ph2\t$phase1\t$phase2\t$_";
}
close INFILEa;
close OUTFILE;


open INFILEa,"fusion_point_3_2_complete_c_title2_orig2_nogap_short";
open OUTFILE,">fusion_point_3_2_complete_c_title2_orig2_nogap_short_phase";
while(<INFILEa>)
{
@a=split(/\t/,$_);
@b=split(/:/,$a[2]);
$phase1=$hash{$b[3]};
$phase2=$hash{$b[4]};

@c=split(/\|/,$a[2]);
$ph1=(3-abs($c[1]))%3;
$ph2=(3-abs($c[3]))%3;


printf OUTFILE "$ph1\t$ph2\t$phase1\t$phase2\t$_";
}
close INFILEa;
close OUTFILE;




open INFILEa,"fusion_point_3_2_complete_c_title2_orig2_gap_noshort_c";
open OUTFILE,">fusion_point_3_2_complete_c_title2_orig2_gap_noshort_c_phase";
while(<INFILEa>)
{
@a=split(/\t/,$_);
@b=split(/:/,$a[2]);
$phase1=$hash{$b[3]};
$phase2=$hash{$b[4]};

@c=split(/\|/,$a[2]);
$ph1=(3-abs($c[1]))%3;
$ph2=(3-abs($c[3]))%3;


printf OUTFILE "$ph1\t$ph2\t$phase1\t$phase2\t$_";
}
close INFILEa;
close OUTFILE;



open INFILEa,"fusion_point_3_2_complete_c_title2_orig2_gap_short_c";
open OUTFILE,">fusion_point_3_2_complete_c_title2_orig2_gap_short_c_phase";
while(<INFILEa>)
{
@a=split(/\t/,$_);
@b=split(/:/,$a[2]);
$phase1=$hash{$b[3]};
$phase2=$hash{$b[4]};

@c=split(/\|/,$a[2]);
$ph1=(3-abs($c[1]))%3;
$ph2=(3-abs($c[3]))%3;


printf OUTFILE "$ph1\t$ph2\t$phase1\t$phase2\t$_";
}
close INFILEa;
close OUTFILE;

