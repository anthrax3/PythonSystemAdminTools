import os
import fnmatch

# this generator function is like Unix find command - returns generator object
def find_generator(file_pattern,top):
    for path, dirlist, file_names in os.walk(top):
        for name in fnmatch.filter(file_names,file_pattern):
            yield os.path.join(path,name) 

# this generator function is like Unix cat command - returns generator object
def cat_generator(sources):
    for s in sources:
        for item in s:
            yield item

# this generator function is like Unix grep commnad -  returns generator object
def grep_generator(pattern, lines):
    result = re.compile(pattern)
        for line in lines:
            if result.search(line): 
                yield line

# example on finding all files with py extension from the root directory
pyfiles = find_generator("*.py","/")

# example of finding all access.logs in the www directory
logs    = find_generator("access.log*","/usr/www/")
