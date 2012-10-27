from collections import Counter
cnt = Counter()

wwwlog = open('access.log')
ip_column = (line.split()[0] for line in wwwlog)
for word in ip_column: cnt[word] +=1
for k,v in cnt.items():
    if v > 50: print k,v
