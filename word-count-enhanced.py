from pyspark import SparkConf, SparkContext
import collections

# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("WordCounterEnhanced")
sc = SparkContext(conf = conf)

lines = sc.textFile("./spark-sandbox/words/book.txt")
words = lines.flatMap(lambda lines: lines.split()).countByValue()
            
for word, count in words.items():
    print(word + "\t" + str(count))