# in the pyspark interactive shell (sc is automatically created)
from pyspark import SparkConf, SparkContext


# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("FriendByAverage")
sc = SparkContext(conf=conf)

#line = sc.textFile("./spark-sandbox/fake-friends/friends.txt")
line = sc.textFile("./spark-sandbox/fake-friends/friends-2.txt")

# read file test
line.count()

f = line.map(
    lambda line: line.split(",")).map(
        lambda x: (x[2], int(x[3]))).mapValues(
            lambda x: (x, 1)).reduceByKey(
                lambda x, y: (x[0]+y[0], x[1]+y[1]))

# test the result
f.collect()

average_by_age = f.mapValues(lambda x: x[0]/x[1]).collect()

for r in average_by_age:
    print(r)