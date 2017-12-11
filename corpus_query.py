import pandas as pd
import numpy as np

OE_CORPUS='/Users/ZaqRosen/Documents/Corpora/diachronics/OE_lines_corpus.txt'
ME_CORPUS='/Users/ZaqRosen/Documents/Corpora/diachronics/ME_lines_corpus.txt'
OE_SEARCH_CORPUS='/Users/ZaqRosen/Documents/Corpora/diachronics/OE_of_lines_corpus.txt'
ME_SEARCH_CORPUS='/Users/ZaqRosen/Documents/Corpora/diachronics/ME_of_lines_corpus.txt'
OE_COLLOCATES='/Users/ZaqRosen/Documents/computational_ling/class_work/diachronics/OE_collocates.txt'
ME_COLLOCATES='/Users/ZaqRosen/Documents/computational_ling/class_work/diachronics/ME_collocates.txt'


COLUMNS=['txt']
df_OE=pd.read_table(OE_CORPUS, sep='\t', names=COLUMNS, skipinitialspace=True, skiprows=0)
df_ME=pd.read_table(ME_CORPUS, sep='\t', names=COLUMNS, skipinitialspace=True, skiprows=0)

def search_lines(search, dfg, outlist):
        for sent in dfg['txt'].values.tolist():
                if search in str(sent):
                        outlist.append(sent)

def collocates(sentence, search, outlistb):
        sent=sentence.split()
        for itm in sent:
                if itm == search.replace(' ', ''):
                        term=sent[sent.index(itm)+1]
                        if term in ['his', 'the', 'a', 'their', 'her', 'weres', 'mergenneméces', 'holma', 'Hréðles', 'þære', 'medobencemicles', 'his', 'ðæs']:
                                outlistb.append(sent[sent.index(itm)+2])
                        else:
                                outlistb.append(term)

def feed_collocates(inlist, search, outlista):
        for itm in inlist:
                collocates(itm, search, outlista)

OE_SEARCH=[]
search_lines(' on ', df_OE, OE_SEARCH)

ME_SEARCH=[]
search_lines(' on ', df_ME, ME_SEARCH)

#out_OE = pd.DataFrame(np.array(OE_SEARCH).reshape(-1, 1), columns=COLUMNS)
#out_OE.to_csv('/Users/ZaqRosen/Documents/Corpora/diachronics/OE_on_lines.txt', sep='\t', encoding='utf-8')
#out_ME = pd.DataFrame(np.array(ME_SEARCH).reshape(-1, 1), columns=COLUMNS)
#out_ME.to_csv('/Users/ZaqRosen/Documents/Corpora/diachronics/ME_on_lines.txt', sep='\t', encoding='utf-8')


OE_collocates=[]
feed_collocates(OE_SEARCH, ' on ', OE_collocates)

ME_collocates=[]
feed_collocates(ME_SEARCH, ' on ', ME_collocates)

df_OEcollocates = pd.DataFrame(np.array(list(set(OE_collocates))).reshape(-1, 1), columns=['collocate'])
df_MEcollocates = pd.DataFrame(np.array(list(set(ME_collocates))).reshape(-1, 1), columns=['collocate'])
df_OEcollocates.to_csv(OE_COLLOCATES, sep='\t', encoding='utf=8')
df_MEcollocates.to_csv(ME_COLLOCATES, sep='\t', encoding='utf=8')
