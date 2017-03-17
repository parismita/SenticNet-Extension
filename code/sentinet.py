import senticnet4
import ast
import sys
from senticnet4 import senticnet
import sentiwordnet
from sentiwordnet import SentiWordNetCorpusReader
from nltk.corpus import wordnet as wn
 
filename = 'SentiWordNet_3.0.0.txt'

#interfacing to sentiwordnet 
swdnet = {}
'''
swn = SentiWordNetCorpusReader(filename)


for senti_synset in swn.all_senti_synsets():
    l = len(senti_synset.synset.name())
    name = senti_synset.synset.name()[:l-5]
    note = senti_synset.synset.name()[l-4:l-3]
    if name not in senticnet.keys() and note == 'a':
        if float(senti_synset.pos_score) > 0.0 or float(senti_synset.neg_score) > 0.0:
            swdnet[name] = [senti_synset.pos_score, senti_synset.neg_score]

#print len(swdnet)

input_filename=open('output.txt')
with input_filename as f:
    content = f.readlines()
content = [x.strip() for x in content] 

for c in content:
    a1 = str(ast.literal_eval(c)[0])
    a2 = ast.literal_eval(c)[1]
    a = a2[0]-a2[1]
    if a>0.0:
        a = ['positive',a]
    else:
        a = ['negetive',a]
    swdnet[a1] = a
print swdnet['untalented'][0]

good = ['joyful', 'interesting', 'surprising', 'admirable']
bad = ['sad', 'scared', 'angry', 'disgusting']

for k in swdnet.keys():
    tag = []
    for j in range(4):
        n=wn.synsets(k)
        if swdnet[k][1]>0:
            g=wn.synsets(good[j])
            tag.append((max(i.wup_similarity(n[0]) for i in g)))
            #print good[tag.index(max(tag))],tag
        else:
            g=wn.synsets(bad[j])
            tag.append((max(i.wup_similarity(n[0]) for i in g)))
            #print bad[tag.index(max(tag))],tag

    c = []
    if swdnet[k][1]>0:
        if tag.index(max(tag)) == 1 and tag.index(max(tag[0],tag[2],tag[3])) == 2:
            c = tag + ['#interesting','#interesting']
        elif tag.index(max(tag)) == 2 and tag.index(max(tag[0],tag[1],tag[3])) == 1:
            c = tag + ['#surprising','#surprising']
        else:
            q = tag.index(max(tag))
            c = tag + ['#'+ good[q]]
            tag[q] = None
            c = c +['#'+ good[tag.index(max(tag))]]

    
    else:
        if tag.index(max(tag)) == 1 and tag.index(max(tag[0],tag[2],tag[3])) == 2:
            c = tag + ['#scared','#scared']
        elif tag.index(max(tag)) == 2 and tag.index(max(tag[0],tag[1],tag[3])) == 1:
            c = tag + ['#angry','#angry']
        else:
            q = tag.index(max(tag))
            c = tag + ['#'+ bad[q]]
            tag[q] = None
            c = c +['#'+ bad[tag.index(max(tag))]]

    swdnet[k] = c + swdnet[k]

print swdnet

'''
s = {}
input_filename=open('output2.txt')
with input_filename as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    a1 = str(ast.literal_eval(c)[0])
    a2 = ast.literal_eval(c)[1]
    #for i in range(8):
    #	if a2[i] == None:
    #	    a2[i] = 0.0
    swdnet[a1] = a2
    print a2
    if a2[9] == a2[10] or a2[11] == a2[12]:
    	del swdnet[a1]
    '''
    sim = []
    for k in senticnet.keys():
        n=wn.synsets(k)
        if n:
            g=wn.synsets(a1)
            sim.append((max(i.path_similarity(n[0]) for i in g)))

    for i in range(5):
        q = sim.index(max(sim))
        swdnet[a1] = swdnet[a1] + [senticnet.keys()[q]]
        if sim[q] == None:
            s[a1] = swdnet[a1]
            del swdnet[a1]
            break
        sim[q] = 0.0
    print a1
            

for a1 in s.keys()
	for senti_synset in swn.all_senti_synsets():
	    l = len(senti_synset.synset.name())
	    k = senti_synset.synset.name()[:l-5]
	    n=wn.synsets(k)

	    if n:
	        g=wn.synsets(a1)
	        sim.append((max(i.path_similarity(n[0]) for i in g)))

	for i in range(5):
	    q = sim.index(max(sim))
	    swdnet[a1] = swdnet[a1] + [senticnet.keys()[q]]
	    if sim[q] == None:
	        s[a1] = swdnet[a1]
	        del swdnet[a1]
	        break
	    sim[q] = 0.0
	print a1

  
'''
output_filename=open('output3.txt','w')
for i in swdnet.items():
    output_filename.write(str(i))
    output_filename.write('\n')
output_filename.close()
 
'''
for key in swdnet.items():
    print key
    #if key in senticnet.key():
    #    print key
for key in senticnet.items():
    print key'''
