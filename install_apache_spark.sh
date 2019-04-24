#install java8
sudo apt update && sudo apt -y upgrade
sudo apt install -y openjdk-8-jdk

#install python
sudo apt install -y python3
sudo apt install -y python3-pip

#install spark 2.4 for linux
wget http://archive.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
tar -xvzf spark-2.4.0-bin-hadoop2.7.tgz

#if u instal python3x, spark seeks for python command. so we should define alias.

echo 'export PYSPARK_PYTHON=python3' >> .profile
source .profile
echo 'export PATH=$PATH:~/spark-2.4.0-bin-hadoop2.7/bin' >> .profile

source ~/.profile

#test pyspark
pyspark

#define in the shell, sc.version
