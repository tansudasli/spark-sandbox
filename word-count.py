from pyspark import SparkConf, SparkContext
import collections

# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("WordCounter")
sc = SparkContext(conf = conf)

lines = sc.textFile("./spark-sandbox/word/starwars.txt")
words = lines.flatMap(lines.split()).map(lambda w: (w,1))