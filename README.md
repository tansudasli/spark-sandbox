# spark-sandbox

## How to start
create a GCP (ubuntu 18.04) instance on GCP console, then connect with that server via appropriate SSH ways.
* `gcloud compute --project .... ssh --zone .... ....`

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

###### 6- download movielens sample data set.
`sudo apt install unzip`<br>
`wget http://files.grouplens.org/datasets/movielens/ml-100k.zip`<br>
`unzip ml-100k.zip`

for latest data-set, you may use *http://files.grouplens.org/datasets/movielens/ml-latest.zip* url. 

##### 7- you may want to write pyspark, and other staffs on your local machine without install spark. There are many ways for that, but i prefer anaconda! 
- [ ] install everything seperately on local (vscode or another IDE, python3, pip3) and jupiyer-notebook and pyspark
- [x] install anaconda on local (w/ conda package manager), then leverage jupiter-notebooks and install pyspark
- [x] don't install pyspark, you will see some imports errors in your IDE and also you won't test code interactively, but that's ok. Run your code on GCP instance where you installed spark.

for anaconda<br>
 `brew cask install anaconda` install anaconda w/ brew on Mac<br>
 `echo 'export PATH="/usr/local/anaconda3/bin/:$PATH"' >> .zshrc` chanche .profile if not using zsh-terminal!<br>
 `cd ~/anaconda3/bin` <br>
 `./conda update -n base -c defaults conda`<br>
 `./conda install -c conda-forge pyspark`<br>


