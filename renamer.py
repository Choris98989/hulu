import os

# Set the directory where your photo files are located
directory = 'c:\\ren'

# The prefix for the files you want to rename (keep the underscore if it's part of the prefix)
prefix = 'baner_'
# The file extension
extension = '.jpg'

# Get a list of all files in the directory that match the prefix and extension
files = [f for f in os.listdir(directory) if f.endswith(extension)]
#print(files)
# Sort the files to ensure the renaming is done in order
files.sort()

# Start the numbering from 1
new_number = 1

for filename in files:
    # Create the new file name
    new_filename = f"{prefix}{new_number}{extension}"
    
    # Full path for current and new filename
    old_file = os.path.join(directory, filename)
    new_file = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_file, new_file)
    
    # Increment the number for the next file
    new_number += 1

print("Files have been renamed.")
