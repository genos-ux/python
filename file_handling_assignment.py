# File Creation:
# Create a Python script (file_handling_assignment.py) that does the following:
# Creates a new text file named "my_file.txt" in write mode ('w').
# Write at least three lines of text to the file, including a mix of strings and numbers.


file = open('my_file.txt','w')
file.write('This is a new string1\n')
file.write('Working with files with python3')
file.write('This is the last one3\n')

# File Reading and Display:
# Enhance your script to read the contents of "my_file.txt" and display them on the console.

file_content =  open('my_file.txt','r')
file_name = file_content.read()
print(file_name)

# File Appending:
# Modify the script to open "my_file.txt" in append mode ('a').
# Append three additional lines of text to the existing content.

file_append = open('my_file.txt','a')
file_append.write('Programming is cool\n')
file_append.write('Python is so cool\n')
file_append.write('C is also cool\n')



