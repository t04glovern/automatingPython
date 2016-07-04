import shutil, os

os.chdir('.\\file-working')

shutil.copy('spam.txt', '.\\delicious')
shutil.copy('eggs.txt', '.\\delicious\\eggs2.txt')

# Backup \delicious\ directory to \delicious_backup\
shutil.copytree('.\\delicious', '.\\delicious_backup')
