import json

f = open('gendered_words.json')

data = json.load(f)

word_list = []

for ele in data:
    if ele['gender'] == 'f' or ele['gender'] == 'm':
        word_list.append(ele['word'])

f.close()

outfile_name = 'gendered_vocab.txt'

with open(outfile_name, 'w+') as f:
    for ele in word_list:
        f.write(ele + '\n')

f.close()