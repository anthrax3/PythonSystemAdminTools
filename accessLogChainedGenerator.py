from collections import Counter

wwwlog = open('access.log')
ip_column = (line.split()[0] for line in wwwlog)
cnt = Counter (ip_column)
for k,v in cnt.items():
    if v > 50: print k,v
