import re

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search("Batman and Tina Fey.")
print(mo1.group())

mo2 = heroRegex.search("Tina Fey and Batman.")
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))