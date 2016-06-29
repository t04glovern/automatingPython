import re

xmasRegex = re.compile(r'\d+\s\w+')
# \d+ = one or more numeric digits between 0-9
# \s = space, tab or newline character
# \w+ = one or more letters or numeric digits, characters or underscores
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)