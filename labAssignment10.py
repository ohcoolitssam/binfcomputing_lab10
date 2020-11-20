#!/usr/bin/env python

#regular expressions are imported
import re

#the original pdb file is opened and its lines are read and set to lines
with open("1fn3.pdb") as f:
	lines = f.readlines()

#dictionary is made
list1 = ['PHE','LEU','SER','TYR','CYS','PRO','HIS','GIN','ARG','SER','ASN','LYS','THR','IIE','MET','GLY','ASP','GLU','ALA','VAL']
list2 = ['UUU','UUA','UCC','UAU','UGU','CCC','CAU','CAA','CGC','AGU','AAU','AAA','ACC','AUU','AUG','GGT','GAC','GAA','GCC','GUU']
triNuc = zip(list1,list2)
dictionary = dict(triNuc)

#reference lists for title, authors, info, source, and codons are created
t = []
a = []
i = []
s = []
c = []

#for loop that grabs important lines from the lines read in from the pdb file
for x in lines:
	l = x.split(" ")
	z = ''
	while z  in l: l.remove('')

	if(re.search(r'HEADER',l[0])):
		i.append(l)
	if (re.search(r'TITLE',l[0])):
		t.append(l)
	if (re.search(r'AUTHOR',l[0])):
		a.append(l)
	if (re.search(r'EXPDTA',l[0])):
		m = l
	if (re.search(r'SOURCE',l[0])):
		s.append(l)
	if (re.search(r'SEQRES',l[0])):
		c.append(l[4:len(l)])	

#output protein name is set to protein
protein = t[0][6]

#output title is set to title
t[0] = t[0][1:len(t[0])-1]
t[1] = t[1][2:len(t[1])-1]
t[0] = " ".join(t[0])
t[1] = " ".join(t[1])
title = " ".join(t)

#output authors are set to authors
a[0] = a[0][1:len(a[0])-1]
a[0] = " ".join(a[0])
authors = " ".join(a)

#output method is set to method
m = m[1:3]
m = " ".join(m)
method = m

#ouput source is set to source
s[1] = s[1][3:5]
s[1][1] = s[1][1][0:7]
s[1] = " ".join(s[1])
s = s[1]
source = "".join(s)

#codons list is created
codons = []
#for loop that converts each codon in the c list to its rna alternate
for z in range(0,len(c)):
	c[z] = c[z][0:len(c[z])-1]
	for q in range(0,len(c[z])):
		for v in range(0,len(list1)):
			if list1[v] == c[z][q]:
				codons.append(dictionary.get(c[z][q]))
			else:
				continue
#translated codons are joined together to form an rna sequence
codons = "".join(codons)

#outut file anme 1FN3.info is opened and all the output information
#is written to the new file
with open('1FN3.info','w') as f:
	f.write("Protein Title: " + title + "\n")
	f.write("Authors: " + authors + "\n")
	f.write("Protein Name: " + protein + "\n")
	f.write("Source of Protein: " + source + "\n")
	f.write("Method used to determine the Structure: " + method + "\n")
	f.write("Here is the RNA Sequence of Hemoglobin: " + codons + "\n")

