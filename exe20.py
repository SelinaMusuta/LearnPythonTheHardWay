from sys import argv

script, input_file = argv

#Create a function called print all that will read a file
def print_all(f):
	print f.read()

# Create a function that will start from the beginnin of a line
def rewind(f):
	f.seek(0)

# Create a function that will read a line and print that line
def print_a_line(line_count, f):
	print line_count, f.readline()

# Open the current file
current_file = open(input_file)

print "First let's print the while file:\n"

# Print the entire text from the document
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Seek document?
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)