# spark-sandbox

## How to start
create a GCP (ubuntu 18.04) instance on GCP console, then connect with that server via appropriate SSH ways.
* 'gcloud compute --project .... ssh --zone .... ....'

###### 1- upload *install_apache_spark.sh* or *tansudasli/spark-sandbox* to GCP instance via
`wget https://raw.githubusercontent.com/tansudasli/spark-sandbox/master/install_apache_spark.sh`

###### 2- then give run permisson to install_cloudera_stack.sh file
`chmod +x install_apache_spark.sh` 

###### 3- and run below script to install python3x, java8 and spark 2.4
`./install_apache_spark.sh` 

if you face w/ connection or downloading issues, run it again after delete unnecessary folders.

###### 4- test pyspark
`pyspark`
and in the shell type, `sc.version`

###### 5- test scala-shell
`spark-shell`
and in the shell type, `sc.version`

###### 6- open portts on GCP Firewall for *default network*
* 7077


