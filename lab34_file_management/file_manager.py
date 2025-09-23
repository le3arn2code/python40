import os
import shutil

# Define source and destination
source = '/home/toor/Downloads'
destination = '/home/toor/Documents/Backup'

# List files in source directory
files = os.listdir(source)
print("Files in source directory:", files)

# Ensure destination directory exists
if not os.path.exists(destination):
    os.makedirs(destination)

# Copy and rename files with _backup suffix
for file in files:
    base, extension = os.path.splitext(file)
    new_name = f"{base}_backup{extension}"
    shutil.copy(os.path.join(source, file), os.path.join(destination, new_name))

print(f"All files copied and renamed to {destination}")
