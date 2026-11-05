import os

# Ask the user for a filename
filename = input("Enter filename to open: ")

# Check whether the file exists
if os.path.exists(filename):
    with open(filename, "r") as data:
        print("\nFile Content:")
        print(data.read())
else:
    print("File not found. Please check the filename.")