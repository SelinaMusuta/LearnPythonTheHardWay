from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these to on one line, how?

in_file = open(from_file)
indata = in_file.read()
