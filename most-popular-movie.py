from pyspark import SparkConf, SparkContext

# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("MostPopularMovie")
sc = SparkContext(conf = conf)

# for a better written code check, aws-emr-jupiter-notebooks/most-popular-movie.ipynb file.
# using collectAsMap() function, we can transform an RDD to Dictionary. 
# So it is mucj more concise !


#broadcast movienames to all executers, for meaningful movie ids
#movie-id|movie-name|movie-date|imdb-url|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0
def loadMovieNames():
    movieNames = {}
    f = open("./spark-sandbox/datasets/ml-100k/u.item", "r", encoding="utf-8", errors="ignore")
    lines = f.readlines()
    for line in lines:
        fields = line.split("|")
        movieNames[int(fields[0])] = fields[1]
    return movieNames
 
#broadcast master dataset
nameDictionary = sc.broadcast(loadMovieNames())

#user-id,movie-id,rating,timespamp
lines = sc.textFile("./spark-sandbox/ml-100k/u.data")
movies = lines.map(
    lambda x: x.split()).map(
        lambda x: (int(x[1]), 1)).reduceByKey(
            lambda x,y: (x+y)).map(
                lambda x: (x[1], x[0])).sortByKey().map(
                    lambda x: (nameDictionary.value[x[1]], x[0])).collect()


for key, value in movies:
    #movie-name popularity
    print("%s %i" % (key, value))
