import os
import os.path
import sys

#check the existence of locations.txt and config.txt
if os.path.isfile("locations.txt") == False:
    #create an empty locations.txt snd stop the program
    open("locations.txt", "w")
    print("ERROR: locations.txt does not exist. Make sure it is in the same directory as this script. A blank file named locations.txt has now been created.")
    sys.exit(1)
if os.path.isfile("config.txt") == False:
    #create a config.txt with default settings (10 days)
    newconfig = open("config.txt", "w+")
    newconfig.write("10\nd")
    newconfig.close()
    print("WARNING: config.txt does not exist. A config.txt has been created with default settings (delete files older than 10 days)")
#load in the locations of directories to be purged
locations = [line.rstrip('\n') for line in open("locations.txt")]
print("Directories to scan:")
for i in range(0, len(locations)):
    print(str(i) + ": " + locations[i])
#if locations.txt is empty, then stop execution
if len(locations) == 0:
    print("ERROR: locations.txt is empty.")
    sys.exit(2)
#load in values from config.txt
config = open("config.txt")
maxagestr = config.readline()
maxage = 10
#try to load in the maximum age of the file, but use 10 if the value in line one of config.txt is invalid
#the "maxiumum age" is how old the file must be before it is deleted
try:
    maxage = int(maxagestr.rstrip('\n'))
except:
    print("WARNING: the value for maximum file age in config.txt is invalid.  Using default value (10).")
    maxage = 10
print("Maximum age of file:\n" + str(maxage))
#load in the unit of time to be used for the maximum age
unitoftime = config.read(1)
print("Unit of time:\n" + unitoftime)
