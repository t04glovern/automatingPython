import shutil

# move bacon.txt to \eggs\
shutil.move('.\\file-working\\bacon.txt', '.\\file-working\\eggs')
# move back
shutil.move('.\\file-working\\eggs\\bacon.txt', '.\\file-working')

# move while renaming bacon.txt to new_bacon.txt to \eggs\new_bacon.txt
shutil.move('.\\file-working\\bacon.txt', '.\\file-working\\eggs\\new_bacon.txt')
# move back
shutil.move('.\\file_working\\eggs\\new_bacon.txt', '.\\file-working')