import pandas as pd
import numpy as np
import codecs

doc=codecs.open('/Users/ZaqRosen/Documents/Corpora/diachronics/_raw/OE_beowulf.txt', 'r', 'utf-8')
searchline=doc.readlines()
text=''
for i, line in enumerate(searchline):
	a=line.replace('    ', ' ').replace('\n', ' ')
	text+=a

doc.close()

	
abacus=text.split('. ')
abacus2=[]
abacus3=[]
for it in abacus:
	if '!' in it:
		a=it.split('! ')
		for itm in a:
			abacus2.append(itm)
	else:
		abacus2.append(it)

		
for it in abacus2:
	if '?' in it:
		a=it.split('? ')
		for itm in a:
			abacus3.append(itm)
	else:
		abacus3.append(it)

abacus4=[]		
for it in abacus3:
	a=it.replace('\xa0', '').replace('  ', ' ')
	abacus4.append(a)

	
df_data=pd.DataFrame(np.array(abacus4).reshape(-1, 1), columns=['text'])
df_data.to_csv('/Users/ZaqRosen/Documents/Corpora/diachronics/OE_corpus_beowulf.txt', sep='\t', encoding='utf-8')
