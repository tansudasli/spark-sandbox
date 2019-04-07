from pyspark import SparkConf, SparkContext
import collections

# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

#stationid,date,entryType,celsius,,,,
lines = sc.textFile("./spark-sandbox/weather/year-1800.txt")
weathers = lines.map(lambda line: line.split(',')).map(
    lambda x: (x[0], x[2], x[3]))
    