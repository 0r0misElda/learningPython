# Global module imports
import os
import json
import sys

# Function to iterate over files in a given path
# Determines if file, directory, or a child directory, and size of tile, in bytes
def path_listing(path):
    p = {'name': (path)}
    if os.path.isdir(path):
        p['type'] = "directory"
        p['child'] = [path_listing(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        p['type'] = "file"
        p['size'] = str(os.path.getsize(path)) + ' B'
    return p

# Receives input from the user to determine which path to anaylze
direc = sys.argv[1]

# Outputs results of fuction in "pretty" JSON format
print (json.dumps(path_listing(direc),indent=2))