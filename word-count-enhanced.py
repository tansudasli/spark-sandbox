import re
from pyspark import SparkConf, SparkContext


# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("WordCounterEnhanced")
sc = SparkContext(conf = conf)

lines = sc.textFile("./spark-sandbox/words/books.txt")

words = lines.flatMap(
    lambda lines: re.compile(r'\w+', re.UNICODE).split(lines.lower())).map(
        lambda word: (word,1)).reduceByKey(
            lambda x,y: x+y).collect()
            
for word, count in words.items():
    print(word + "\t" + str(count))