#!/usr/bin/env python

import string
import urllib
import re
import sys
import webbrowser
import os


print   '############################################################'
print   '#                                                          #'
print   '#            ###################################           #'
print   '#            #   WELCOME TO THE DALI RIPPER    #           #'
print   '#            ###################################           #'
print   '#                                                          #'	    
print   '#      THIS SMALL PROGRAM WILL OUTPUT TOP 50 DALI HITS     #'
print   '#         AS .PDB INTO THE FOLDER YOU RUN THE SCRIPT       #'
print   '#                                                          #'
print   '#                                                          #'
print   '#           FILES ARE NAMED IN THE FOLLOWING MANNER:       #'
print   '#                                                          #'
print   '#                ZSCORE-PDBID-CHAINID-PROTEIN.PDB          #'
print   '#                                                          #'
print   '############################################################'
	    

Dali_URL = raw_input('Please paste in your Dali results URL: ')
data_dump = urllib.urlopen(Dali_URL).read()

PDB = (re.findall('pdbid=(.*)&chainid=', data_dump))

Chain_ID = re.findall('cd2=(.*) sequence=', data_dump)
Chain_letter = []
for item in Chain_ID:
	letter = item[4:5]
	Chain_letter.append(letter)

Molecule_ID = re.findall('  MOLECULE: (.*)   ', data_dump)
Protein_name = []
for item in Molecule_ID:
	name = item[0:49]
	Protein_name.append(name)
formated_name = [i.split(';', 1)[0] for i in Protein_name]
final_names = [i.split('  ', 1)[0] for i in formated_name]
final_names2 = [i.replace(' ','_') for i in final_names]
final_names3 = [i.replace('/','_') for i in final_names2]

Z_score = re.findall('</A> (.*) <A HREF=', data_dump)
score = [i.split()[0] for i in Z_score]

final_file = zip(score, PDB, Chain_letter, final_names3)[0:99]

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


for i in final_file:
	website = 'http://ekhidna.biocenter.helsinki.fi/dali_server/qz-test?jobid=pdb&pdbid=' + i[1]
	file_name = '_'.join(i)
	file_name_pdb = file_name +'.pdb'
	print file_name_pdb
	tmp = urllib.urlopen(website).read()
	tmp_fasta = urllib.urlopen(website).readlines()
	file = open(file_name_pdb,'w')
	file.write(tmp)
	file.close()
	
