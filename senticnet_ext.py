import senticnet4
import ast
import sys
from senticnet4 import senticnet
import sentiwordnet
from sentiwordnet import SentiWordNetCorpusReader
from nltk.corpus import wordnet as wn

swdnet = {}

input_filename=open('final_output.txt')
with input_filename as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    a1 = str(ast.literal_eval(c)[0])
    a2 = ast.literal_eval(c)[1]
    swdnet[a1] = a2

print swdnet