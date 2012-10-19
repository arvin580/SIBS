open INFILE,"<hct.rko.file";
open OUTFILE_a,">runtandem.pbs";
while(<INFILE>)
{
	chomp($_);
	s/\r$//g;
	if(/mgf$/)
	{
		$xml=$_;
                $xml=~s/mgf/xml/g;
		$outfile_a="input_$xml";
		$outfile_b="output_$xml";
		open OUTFILE,">$outfile_a";
		printf OUTFILE "<?xml version=\"1.0\"?>\n";
		printf OUTFILE "<bioml>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, parent monoisotopic mass error plus\">20</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, parent monoisotopic mass error minus\">20</note>\n";
		printf OUTFILE "\n";
		printf OUTFILE "\t<note type=\"input\" label=\"list path, default parameters\">default_input.xml</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"list path, taxonomy information\">taxonomy.xml</note>\n";
		printf OUTFILE "\n";
		printf OUTFILE "\t<note type=\"input\" label=\"protein, taxon\">homo sapiens</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, path\">input\/$_</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"output, path\">output2\/$outfile_b</note>\n";
		printf OUTFILE "</bioml>\n";
		printf OUTFILE_a "inputxml2\/$outfile_a\n";

		close OUTFILE;

	}
}
close INFILE;
close OUTFILE_a;
