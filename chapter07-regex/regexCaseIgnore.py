import re

robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop.')
print(mo.group())

mo = robocop.search('ROBOCOP protects the innocent.')
print(mo.group())

mo = robocop.search('Al, why does your programming book talk about robocop so much?')
print(mo.group())