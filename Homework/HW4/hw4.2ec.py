#!/usr/bin/env python3
word_dict = set()
count = 0

fo = open('../python_data/words.txt')
fo_2 = open('../python_data/sawyer.txt')


for word in fo:
    word_dict.add(word.rstrip('\n'))

print('{word_dict} words in spelling words'.format(word_dict=len(word_dict)))
print('\n')

fo_2_read = fo_2.readlines()
fo_2_split = fo_2.splitlines('\n')
print(fo_2_split)

# for sawyer_words in fo_2_read:
#     count += 1
#     for words in fo_2_split:
#         if words.lower().rstrip(',.:;?') in word_dict:
#             continue
#         else:
#             print('mispelled word on line {count}: {sawyer_words}'.format(count= count, sawyer_words=words.lower().rstrip(',.:;?!')))

fo.close()
fo_2.close()
print(count)
