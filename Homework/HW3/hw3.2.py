#!/usr/bin/env python3

sawyer_doc = open("../python_data/sawyer.txt")

text = sawyer_doc.read()

lines = text.splitlines()
words = text.split()

lines_count = len(lines)

word_count = len(words)

characater_count = len(text)

sawyer_doc.close()

print(lines_count, word_count, characater_count)
