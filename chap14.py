# This is where chapter 14 exercises go.

# Exercise 14.6

import urllib

print 'Please enter in a zip code.'
print 'The corresponding location and population will be given.'
zip_code = raw_input('> ')
conn = urllib.urlopen('http://www.uszip.com/zip/'+zip_code)
for line in conn:
	if line.strip()[:7] == '<title>':
		name = line.strip()[7:]
		name = name[:-17]
		if name == ', ':
			print 'No location found'
		else:
			print name 
	if 'Total population' in line.strip():
		indexor = line.strip()
		indexor2 = indexor
		indexor = indexor.find('Total population')
		indexor2 = indexor2[indexor+25:]
		indexor2 = indexor2.find('<')
		population = line.strip()[indexor+25:indexor+25+indexor2]
		print population



