from os import mkdir, listdir, getcwd
from shutil import move

"""
Concepts required:
    * for loops
    * conditionals
    * lists
    * paths
    * substrings

Description
-------
Included in the exercise is a zipfile, 'files.zip'. It contains 200 files with random character strings for names, all lowercase. First, unzip this file into a directory named 'original_files'.

Your job is to write a program, ex1.py, that does the following things:

1. Create 26 directories in the current directory, one for each letter of the alphabet:
    ./a/
    ./b/
    ./c/
    etc.

2. Loop through all the files in the original_files directory, and organize each of those files into the directory that their name starts with.

### Example:
    The file named 'artichoke.txt' would go into the directory 'a',
    'bartholomew.txt' would go into 'b'.
"""

for num in range(97, 123):
	letter = chr(num)
	mkdir(letter)

files = listdir("./original_files/")

for each_file in files:
	destination = "./" + each_file[0] + "/" + each_file
	source = "./original_files/" + each_file
	move(source, destination)
