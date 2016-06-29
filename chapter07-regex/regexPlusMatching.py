import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search("The Adventures of Batman")
print(mo1 == None)

mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())

mo3 = batRegex.search("The Adventures of Batwowowowowoman")
print(mo3.group())