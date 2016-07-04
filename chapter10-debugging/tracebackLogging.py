import traceback

errorPath = '.\\file-working\\errorInfo.txt'

try:
    raise Exception('This is the error message.')
except:
    errorFile = open(errorPath, 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to ' + errorPath)