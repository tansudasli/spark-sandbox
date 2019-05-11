# spark-sandbox

for a brief introduction to [streams](https://github.com/tansudasli/spark-sandbox/wiki/Streaming-Fundamentals)<br>

## How to run spark

spark can be run in many ways. I did on AWS EMR, Dataproc on GCP, Computing Instance on GCP and Serverless Databricks.

- [x] standalone, on GCP<br> 
      here, you should do some steps on GCP (step-1,2,3,4,5) and on your local machine (step-6)<br> 
      also, open ports: 7070, 4040 on GCP instance firewall
- [ ] standalone, on your local machine
- [x] standalone, on your local machine w/ anaconda and pyspark package installation (step-6)
- [x] master-slave, on GCP<br> 
    here, you should do some steps on GCP (step-1,2,3,4,5,8) and on your local machine (step-6)<br> 
    also, open ports: 7070, 8080, 8081 on GCP instance firewall
- [x] master-slave, on **AWS EMR**<br> 
    look for details under */aws-emr-jupiter-notebooks/README.md* file. You have to pay, either use or not use, but 2 optimization is available. <br>
        * EMR instances are %50 discounted compared to EC2 equivalant instances<br>
        * Leverage spot instances for more cost decrease.<br>
        * Use transient instances for job kind things
- [x] master-slave, on **GCP Dataproc**<br> 
    very similar to AWS, except more robust and more faster and much better experience in GCP. <br>
       * Do not forget to add Jupiter component installation and open 8123 port on firewall ! <br>
       * Leverage preemptible instances for more cost decrease.<br>
       * Use transient instances for job kind things
- [ ] master-slave, on your local machine
- [x] Serverless Databricks on Azure<br> 
     look for details under */databricks-jupiter-notebooks/README.md* file. You only pay,when you process.
- [ ] Serverless Databricks on AWS

## How to start

**Basicly**,

* copy your dataset
* get your spark cluster
* do your things in jupiter
* submit your job to cluster 

0- create a GCP (ubuntu 18.04) instance on GCP console, then connect with that server via appropriate SSH ways.
* `gcloud compute --project .... ssh --zone .... ....`

1- upload *install_apache_spark.sh* or *tansudasli/spark-sandbox* to GCP instance via

 `wget https://raw.githubusercontent.com/tansudasli/spark-sandbox/master/install_apache_spark.sh`

2- then give run permisson to install_cloudera_stack.sh file

 `chmod +x install_apache_spark.sh` 

3- and run below script to install python3x, java8 and spark 2.4
 `./install_apache_spark.sh` 

if you face w/ connection or downloading issues, run it again after delete unnecessary folders.

4- test pyspark in *standalone, on GCP*
`pyspark` for python or `spark-shell` for scala<br>
and then, in the shell, type `sc.version`

    * at this stage you may access your spark over `IP:4040` to see jobs and storages etc.

5- download movielens sample data set.
 `sudo apt install unzip`<br>
 `wget http://files.grouplens.org/datasets/movielens/ml-100k.zip`<br>
 `unzip ml-100k.zip`

for latest & largest data-set, you may use *http://files.grouplens.org/datasets/movielens/ml-latest.zip* url. 

6- you may want to write pyspark, and other staffs on your local machine without install spark. There are many ways for that, but i prefer anaconda! 

- [ ] install everything seperately on local (vscode or another IDE, python3, pip3) and jupiyer-notebook and pyspark
- [x] don't install pyspark, you will see some imports errors in your IDE and also you won't test code interactively, but that's ok. Run your code on GCP instance where you installed spark.
- [x] install anaconda on local (w/ conda package manager), then leverage jupiter-notebooks and install pyspark

for anaconda <br>
 `brew cask install anaconda` install anaconda w/ brew on Mac<br>
 `echo 'export PATH="/usr/local/anaconda3/bin/:$PATH"' >> .zshrc` chanche .profile if not using zsh-terminal!<br>
 `cd ~/anaconda3/bin` <br>
 `./conda update -n base -c defaults conda` <br>
 `./conda install -c conda-forge pyspark` <br>

    * on VSCode, do not forget to switch python interpreter to anaconda python version!

8- you may want to test *master-slave, on GCP*, then run below commands.
  `./sbin/start-master.sh` <br> 
  `./sbin/start-slave.sh spark://IP:7077` <br> 
  `pyspark --master spark://IP:7077`

9- to run jupiternotebook on GCP instance,
 `sudo pip3 install runipy`<br>
 `runipy  spark-sandbox/ratings-histogram.ipynb`
