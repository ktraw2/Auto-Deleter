import os.path
import sys

#check the existence of locations.txt and config.txt
if os.path.isfile("locations.txt") == False:
    #create an empty locations.txt snd stop the program
    open("locations.txt", "w")
    print("ERROR: locations.txt does not exist. Make sure it is in the same directory as this script! A blank file named locations.txt has now been created.")
    sys.exit(1)
if os.path.isfile("config.txt") == False:
    #create a config.txt with default settings (10 days)
    newconfig = open("config.txt", "w+")
    newconfig.write("10\nd")
    newconfig.close()
    print("WARNING: config.txt does not exist. A config.txt has been created with default settings (delete files older than 10 days)")
#load in the locations of directories to be purged
locations = [line.rstrip('/n') for line in open("locations.txt")]
for i in range(0, len(locations)):
    print(str(i) + ": " + locations[i])
