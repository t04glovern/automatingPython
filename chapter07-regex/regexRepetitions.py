import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search("HaHaHaHa")
print(mo1.group())

# Greedy vs Non-Greedy

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())