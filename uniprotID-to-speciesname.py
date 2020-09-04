import string
import urllib
import re
import sys
import webbrowser
import os
import itertools

print 		'############################################################'
print  		'#                                                          #'
print  		'#              ################################            #'
print  		'#              #    uniprotID-to-speciesname  #            #'
print 		'#              ################################            #'
print 		'#                                                          #'	    
print     	'#    THIS PROGRAM WILL ACCEPT FASTA FILES WITH ACCENSION   #'
print     	'#             CODES AS THE NAME OF THE SEQUENCE            #'
print     	'#                                                          #'
print     	'#                      E.G (> A0A014NDI1)                  #'
print     	'#           						    #'
print     	'#  IT WILL THEN CHANGE THE ACCENSION CODE FOR THE SPECIES  #'
print		'#	NAME AND RETURN THE SEQUENCES AS A .TXT FILE        #'
print     	'#                					    #'
print     	'############################################################'


def FASTA_title(text):
	key_list = text.keys()
	return key_list
			
def species_search_from_ID(text):
	URL = []
	species_list = []
	for ID in text:
		URL_list = 'http://www.uniprot.org/uniprot/'+ID
		URL.append(URL_list)
	for line in URL:
		urlsearch = urllib.urlopen(line).read()
		species_name = re.findall(' OS=(.*) GN=', urlsearch)
		function_name = str(re.findall('property="schema:name">(.*)</h1></div>', urlsearch))
		species_name = str(species_name + function_name).replace("'", '').replace(', ','_')
		print species_name
		species_list.append(species_name)
	return species_list
	
def oneDArray(text):
    return list(itertools.chain(*text))

# function contributed by C.J.C
def read_fasta_file(file,wholeLabelLine=0,allowDuplicates=0):

  # set allowDuplicates=1 when call if want it not to bomb out for duplicates (by name)
  # which of duplicate pair gets included is undefined

  names_list=[]   # ordered list of names, same order as in file
  seq_dict={}   # dictionary of sequences, keyed by name

  file = sys.argv[1]
  output = sys.argv[2]
  lines=open(file, 'rU').readlines()

  for line in lines:
    isnameline=re.search('^[ ]*>[ ]*([^ ]*)',line)
    isblankline=re.search('^[ ]*$',line)
    #    print isnameline, isblankline, "----",line,"----"
    if isnameline:
      if wholeLabelLine:
        name = line[1:-1]
      else:
        name = re.sub('\n','',isnameline.group(1))
      if not seq_dict.has_key(name):
        seq_dict[name]=''
        names_list.append(name)
      else:
        if not allowDuplicates:
          print 'Duplicate name %s in file %s' % (name,filename)
          sys.exit(1)
    if not (isblankline or isnameline):
      seq_dict[name]+=re.sub(r'(\n| |[0-9])','',line) # CJC added 07feb03 
      #seq_dict[name]+=re.sub('\n','',(re.sub(' ','',line)))
  return seq_dict

if len(sys.argv) <= 1:
	print 'usage: ID_2_species_v0.2.py file.txt'
	exit()

created_dict = read_fasta_file(file, 1, 1) # name, sequence is now in a dictionary
ID = FASTA_title(created_dict) # ID - just a list of the names of FASTAs from the dictionary
species_name = species_search_from_ID(ID) # species_name - list of species names based on their protein ID
species_name_strip = oneDArray(species_name) # species_name_strip removes unnessecary list values from species_name
species_ID = dict(zip(ID, species_name)) # species_ID - creates a dictionary of both protein ID(keys) and species name (value)
file_input = open(sys.argv[1], 'rU').read()
pattern = re.compile(r'\b(' + '|'.join(species_ID.keys()) + r')\b')
result = pattern.sub(lambda x: species_ID[x.group()], file_input)

print result

file_output = open(sys.argv[2], 'w+')
file_output.write(result)
file_output.close()
