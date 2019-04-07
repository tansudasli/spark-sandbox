import re
from pyspark import SparkConf, SparkContext


# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("WordCounterEnhanced")
sc = SparkContext(conf = conf)

lines = sc.textFile("./spark-sandbox/words/book.txt")

words = lines.flatMap(
    lambda lines: re.compile(r'\W+', re.UNICODE).split(lines.lower())).map(
        lambda word: (word,1)).reduceByKey(
            lambda x,y: x+y).map(
                lambda x: (x[1],x[0])).sortByKey().collect()
            
for word, count in words:
    print(str(word) + "\t\t" + str(count))