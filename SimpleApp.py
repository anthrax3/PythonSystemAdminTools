"""
auth log analysis with spark
SimpleApp.py
"""
import sys
from operator import add
from time import strftime
from pyspark import SparkContext

outFile = "counts" + strftime("%Y-%m-%d")
logFile = "auth.log"
destination = "local"
appName = "Simple App"

sc = SparkContext(destination, appName)
logData = sc.textFile(logFile).cache()
failedData = logData.filter(lambda x: 'Failed' in x)
rootData = failedData.filter(lambda s: 'root' in s)

def splitville(line):
    return line.split("from ")[1].split()[0]
    
ipAddresses = rootData.map(splitville)
counts = ipAddresses.map(lambda x: (x, 1)).reduceByKey(add)
output = counts.collect()
for (word, count) in output:
    print "%s: %i" % (word, count)
counts.saveAsTextFile(outFile)

