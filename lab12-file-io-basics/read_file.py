# read_file.py

# Open the file output.txt in read mode
with open('output.txt', 'r') as f:
    # Read each line in the file
    for line in f:
        # Print the line to the console
        print(line.strip())
