import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo2 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo2)