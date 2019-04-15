from pyspark import SparkConf, SparkContext

# you don't need below 2 lines in pyspark interactive shell !
conf = SparkConf().setMaster("local").setAppName("MinWeather")
sc = SparkContext(conf = conf)

#stationid,date,entryType,celsius,,,,
lines = sc.textFile("./spark-sandbox/datasets/weather/year-1800.txt")  #['ITE00100554,18000101,TMAX,-75,,,E,', 'ITE00100554,18000101,TMIN,-148,,,E,']
weathers = lines.map(lambda line: line.split(',')) \
                .map(lambda x: (x[0], x[2], float(x[3])/10)) \
                .filter(lambda x: "TMIN" in x[1]) \
                .map(lambda x: (x[0], x[2])) \
                .reduceByKey(lambda x,y: min(x,y)) \
                .collect()

for weather in weathers:
    print(weather[0] + "\t" + str(weather[1]) + " Celsius")