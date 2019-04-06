from pyspark import SparkConf, SparkContext
import collections

# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("WordCounter")
sc = SparkContext(conf = conf)

lines = sc.textFile("./spark-sandbox/words/starwars.txt")
words = lines.flatMap(
    lambda lines: lines.split()).map(
        lambda word: (word,1)).reduceByKey(
            lambda x,y: x+y).collect()
            
for word in words:
    print(word)