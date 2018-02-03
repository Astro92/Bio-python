#!/usr/bin/env python

import sys

############ FUNCTIONS #############

############ START OF PROGRAM #############

if len(sys.argv) <= 1:
	print 'usage: python pdb2fasta.py file.pdb'
	exit()

pdb_file = open(sys.argv[1]).readlines()

letters = {'ALA':'A','BALA':'A','AALA':'A','ARG':'R','AARG':'R',
		   'BARG':'R','ASN':'N','AASN':'N','BASN':'N','ASP':'D',
		   'AASP':'D','BASP':'D','CYS':'C','ACYS':'C','BCYS':'C',
		   'GLU':'E','AGLU':'E','BGLU':'E','GLN':'Q','AGLN':'Q',
		   'BGLN':'Q','GLY':'G','AGLY':'G','BGLY':'G','HIS':'H',
		   'AHIS':'H','BHIS':'H','ILE':'I','AILE':'I','BILE':'I',
		   'LEU':'L','ALEU':'L','BLEU':'L','LYS':'K','ALYS':'K',
		   'BLYS':'K','MET':'M','AMET':'M','BMET':'M','PHE':'F',
		   'APHE':'F','BPHE':'F','PRO':'P','APRO':'P','BPRO':'P',
		   'SER':'S','ASER':'S','BSER':'S','THR':'T','ATHR':'T',
		   'BTHR':'T','TRP':'W','ATRP':'W','BTRP':'W','TYR':'Y',
		   'ATYR':'Y','BTYR':'Y','VAL':'V','AVAL':'V','BVAL':'V'}

for line in pdb_file:
	element = line.split()
	if element[0] == 'HEADER':
		title = str(element[1]+'_'+element[3].lower())

header = '>' + title.upper().replace('/','-')+'\n'

residues = {}
for line in pdb_file:	
	element = line.split()
	if element[0] != 'ATOM': continue
	if element[4] != 'A': continue
	residues.update({int(element[5]):element[3]})

fasta = {k: letters.get(v, v) for k, v in residues.items()}.values()
fasta = ''.join(fasta)
print fasta

file_name = title.upper().replace('/','_')+'.fasta'
file = open(file_name,'w')
file.write(header)
file.write(fasta)
file.close()
