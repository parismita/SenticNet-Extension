import senticnet4
import ast
import sys
from senticnet4 import senticnet
import sentiwordnet
from sentiwordnet import SentiWordNetCorpusReader
from nltk.corpus import wordnet as wn
 
filename = 'negative-words.txt'
 

swdnet = {}

input_filename=open(filename)
with input_filename as f:
    words = f.readlines()
words = [x.strip() for x in words] 
for word in words:
    if word not in senticnet.keys():
        swdnet[word] = [0.0, 1.0]
input_filename.close()

filename = 'positive-words.txt'
input_filename=open(filename)
with input_filename as f:
    words = f.readlines()
words= [x.strip() for x in words] 
for word in words: 
    if word not in senticnet.keys():
        swdnet[word] = [1.0, 0.0]
input_filename.close()

print len(swdnet)

output_filename=open('output1.txt','a')
for i in swdnet.items():
    output_filename.write(str(i))
    output_filename.write('\n')
output_filename.close()



input_filename=open('output1.txt')
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
print swdnet

good = ['joyful', 'interesting', 'surprising', 'admirable']
bad = ['sad', 'scared', 'angry', 'disgusting']

for k in swdnet.keys():
    tag = []
    if not wn.synsets(k):
        del swdnet[k]
    else:
        for j in range(4):
            n=wn.synsets(k)
            if swdnet[k][1]>0:
                g=wn.synsets(good[j])
                tag.append((max(i.path_similarity(n[0]) for i in g)))
                print good[tag.index(max(tag))],tag
            else:
                g=wn.synsets(bad[j])
                tag.append((max(i.path_similarity(n[0]) for i in g)))
                print bad[tag.index(max(tag))],tag


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



output_filename=open('output.txt','a')
for i in swdnet.items():
    output_filename.write(str(i))
    output_filename.write('\n')
output_filename.close()
