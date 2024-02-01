import keyword

import string

word_input = input()
validator = True
count = 0
count_2 = 0
count_3 = 0

if word_input[0].isdigit() or " " in word_input or word_input.isdigit():
    validator = False

if validator:
    while count < len(word_input):
        if word_input[count].isupper():
            validator = False
            break
        else:
            count += 1

if validator:
    while count_2 < len(keyword.kwlist):
        if word_input != keyword.kwlist[count_2]:
            count_2 += 1
        else:
            validator = False
            break

if validator:
    while count_3 < len(string.punctuation):
        if string.punctuation[count_3] == "_":
            count_3 += 1
            continue
        elif word_input.rfind(string.punctuation[count_3]) >= 0:
            validator = False
            break
        else:
            count_3 += 1

print(validator)
print(keyword.kwlist)
