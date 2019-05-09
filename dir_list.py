import os
import json


def path_listing(path):
    p = {'name': (path)}
    if os.path.isdir(path):
        p['type'] = "directory"
        p['child'] = [path_listing(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        p['type'] = "file"
        p['size'] = str(os.path.getsize(path)) + ' B'
    return p

direc = input("Enter path: ")
print (json.dumps(path_listing(direc),indent=2))