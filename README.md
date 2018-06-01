# bio-python

This is a small package of python scripts that have aided me during my structural biology PhD.

PDB-to-FASTA.py

A python script that will take a standard format .pdb file and output a .fasta file of the protein sequence. The script assumes the protein chain of interest is 'A'.

uniprotID-to-speciesname.py

This script will convert the uniprot ID found within .fasta files, and replace it with the species name instead.
i.e.  >Q63TL0   ----->    >Burkholderia pseudomallei (strain K96243)

Dali-to-PDB.py

A script that will take the URL provided as a result of a dali server search i.e.  http://ekhidna.biocenter.helsinki.fi/dali_server/results/YOUR-RESULT-HERE/index.html
and convert the top 50 results into .pdb files for visulisation and structural alignment. The Dali scores associated to the results will be included in the title of the generated files.
