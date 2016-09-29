# Get the systems package from the arguments variable module
from sys import argv

# Create two argument variables
script, filename = argv

# Create a txt variable to display text 
txt = close(filename)

# Print string to display file text
print "Here's your file %r:" % filename

# Read text
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = close(file_again)

# Remember to call the object ()...without it I'm only calling the object reference
print txt_again.read()