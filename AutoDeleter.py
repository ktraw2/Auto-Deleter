import os.path

#check the existence of locations.txt and config.txt
if os.path.isfile("locations.txt") == False:
    open("locations.txt", "w")
    print("ERROR: locations.txt does not exist. Make sure it is in the same directory as this script! A blank file named locations.txt has now been created.")
if os.path.isfile("config.txt") == False:
    open("config.txt", "w")
    print("WARNING: config.txt does not exist. A confix.txt has been created with default settings (delete files older than 10 days")
#load in the locations of directories to be purged
locations = [line.rstrip('/n') for line in open("locations.txt")]
for i in range(0, len(locations)):
    print(str(i) + ": " + locations[i])
