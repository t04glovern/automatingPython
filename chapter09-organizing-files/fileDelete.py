# Calling os.unlink(path) will delete the file at path.
import os
for filename in os.listdir('.\\file-working'):
    if filename.endswith('.rxt'):
        print(filename)
        ## Run above first to see what files will be affected

for filename in os.listdir('.\\file-working'):
    if filename.endswith('.rxt'):
        os.unlink(filename)


# Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
# Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.
