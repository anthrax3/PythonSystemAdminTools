import os
import fnmatch

# this generator function is like Unix find command - returns generator object
def find_generator(file_pattern,top):
    for path, dirlist, file_names in os.walk(top):
        for name in fnmatch.filter(file_names,file_pattern):
            yield os.path.join(path,name) 

# example on finding all files with py extension from the root directory
pyfiles = find_generator("*.py","/")

# example of finding all access.logs in the www directory
logs    = find_generator("access.log*","/usr/www/")
