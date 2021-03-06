from pyspark import SparkConf, SparkContext

# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("MostPopularMarvelCharacter")
sc = SparkContext(conf = conf)

# for a better written code check, aws-emr-jupiter-notebooks/most-popular-marvel-character.ipynb file.
# using collectAsMap() function, we can transform an RDD to Dictionary. 
# So it is much more concise !

#broadcast marvel character names to all executers
#marvel-hero-id hero-name
def loadMarvelHeroNames():
    marvelHeroNames = {}
    f = open("./spark-sandbox/marvel/marvel-hero-names.txt", "r", encoding="utf-8", errors="ignore")
    lines = f.readlines()
    for line in lines:
        fields = line.split(" ")
        marvelHeroNames[int(fields[0])] = fields[1]
    return marvelHeroNames

#broadcast master dataset
heroDictionary = sc.broadcast(loadMarvelHeroNames())

#marvel-hero-id marvel-hero-id marvel-hero-id marvel-hero-id ....
lines = sc.textFile("./spark-sandbox/datasets/marvel/marvel-graph.txt")
movies = lines.flatMap(lambda line: line.split()) \
            .map(lambda heroID: (heroID, 1)) \
            .reduceByKey(lambda x,y: (x+y)) \
            .map(lambda x: (x[1],x[0])) \
            .max()

#movie-name popularity
print("%s is the most popular marvel hero w/ %i times" % (heroDictionary.value[int(movies[1])], movies[0]))
