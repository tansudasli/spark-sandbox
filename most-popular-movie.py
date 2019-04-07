from pyspark import SparkConf, SparkContext

# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("MostPopularMovie")
sc = SparkContext(conf = conf)

#user-id,movie-id,rating,timespamp
lines = sc.textFile("./spark-sandbox/ml-100k/u.data")
movies = lines.map(
    lambda x: x.split()).map(
        lambda x: (x[1], 1)).reduceByKey(
            lambda x,y: (x+y)).map(lambda x: (x[1], x[0])).sortByKey().collect()


for key, value in movies:
    #movie-id popularity
    print("%s %i" % (value, key))
