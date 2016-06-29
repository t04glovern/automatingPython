import re

noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.'
                      '\nUphold the law.')
print(mo.group())

newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.'
                    '\nUphold the law.')
print(mo.group())