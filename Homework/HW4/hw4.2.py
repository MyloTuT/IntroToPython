#!/usr/bin/env python3
word_dict = set()

fo = open('../python_data/words.txt')
fo_2 = open('../python_data/sawyer.txt')


for word in fo:
    word_dict.add(word.rstrip('\n'))

print('{word_dict} words in spelling words'.format(word_dict=len(word_dict)))
print('\n')

fo_2_read = fo_2.read()
fo_2_split = fo_2_read.split()

for sawyer_words in fo_2_split:

    if sawyer_words.lower().rstrip(',.:;?') in word_dict:
        continue
    else:
        print('mispelled word: {sawyer_words}'.format(sawyer_words=sawyer_words.lower().rstrip(',.:;?!')))

fo.close()
fo_2.close()
