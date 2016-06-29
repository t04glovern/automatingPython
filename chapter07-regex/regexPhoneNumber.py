import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo1 = phoneNumRegex.search("My number is 415-555-4242.")
print("Phone number found: " + mo1.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo2 = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo2)