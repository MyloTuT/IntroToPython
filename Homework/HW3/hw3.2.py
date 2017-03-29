#!/usr/bin/env python3

sawyer_doc = open("../python_data/sawyer.txt")

text = sawyer_doc.read()

lines = text.splitlines()
words = text.split()

line_length = line[0:-1]
length_show = len(line_length)

word = words[0:-1]
word_count = len(word)

truth_count = len(repr(text))

sawyer_doc.close()

print(length_show, word_count, truth_count)
