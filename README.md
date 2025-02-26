# HADOOP-SINGLE-NODE-CLUSTER-IN-UBUNTU

### Step 1 : Install java jdk 8
First of all you must install Java JDK 11 on your system. You can just type this command to install java jdk on your system.
~~~shell
sudo apt install openjdk-8-jdk
~~~
To check it’s there cd /usr/lib/jvm

### Step 2 : Add this configuration on you bash file
Now just open .bashrc file and paste these commands.
to open use the below comand 
~~~shell
nano .bashrc
~~~
now paste this inside the script 
~~~shell
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64 
export PATH=$PATH:/usr/lib/jvm/java-11-openjdk-amd64/bin 
export HADOOP_HOME=~/hadoop-3.4.1/ 
export PATH=$PATH:$HADOOP_HOME/bin 
export PATH=$PATH:$HADOOP_HOME/sbin 
export HADOOP_MAPRED_HOME=$HADOOP_HOME 
export YARN_HOME=$HADOOP_HOME 
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop 
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native 
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native" 
export HADOOP_STREAMING=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar
export HADOOP_LOG_DIR=$HADOOP_HOME/logs 
export PDSH_RCMD_TYPE=ssh
~~~
( ssh — secure shell — protocol used to securely connect to remote server/system — transfers data in encrypted form)

now source the code so that the changes is made
run this after pasting the above comand
~~~shell
source ~/.bashrc
~~~
~~~shell
sudo apt-get install ssh
~~~
now go to hadoop.apache.org website download the tar file
(hadoop.apache.org — download tar file of hadoop.)
~~~shell
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz
~~~
~~~shell
tar -zxvf ~/hadoop-3.4.1.tar.gz 
~~~
(Extract the tar file)
~~~shell
cd hadoop-3.4.1/etc/hadoop
~~~
now open hadoop-env.sh
~~~shell
sudo nano hadoop-env.sh
~~~
~~~shell
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64 
~~~
Step 3 : Add this file in core-site.xml
Now add this configuration in core-site.xml file.

core-site.xml
~~~shell
<configuration> 
 <property> 
 <name>fs.defaultFS</name> 
 <value>hdfs://localhost:9000</value>  </property> 
 <property> 
<name>hadoop.proxyuser.dataflair.groups</name> <value>*</value> 
 </property> 
 <property> 
<name>hadoop.proxyuser.dataflair.hosts</name> <value>*</value> 
 </property> 
 <property> 
<name>hadoop.proxyuser.server.hosts</name> <value>*</value> 
 </property> 
 <property> 
<name>hadoop.proxyuser.server.groups</name> <value>*</value> 
 </property> 
</configuration>
~~~
Step 3 : Add this file in hdfs-site.xml
Now add this configuration in hdfs-site.xml file.

hdfs-site.xml
~~~ shell
<configuration> 
 <property> 
 <name>dfs.replication</name> 
 <value>1</value> 
 </property> 
</configuration>
~~~
Step 4: Add this file in mapred-site.xml
Now add this configuration in mapred-site.xml file.

mapred-site.xml

~~~shell
<configuration> 
 <property> 
 <name>mapreduce.framework.name</name>  <value>yarn</value> 
 </property> 
 <property>
 <name>mapreduce.application.classpath</name> 
  
<value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value> 
 </property> 
</configuration>
~~~
Step 4: Add this file in yarn-site.xml
Now add this configuration in yarn-site.xml file.

yarn-site.xml
~~~shell
<configuration> 
 <property> 
 <name>yarn.nodemanager.aux-services</name> 
 <value>mapreduce_shuffle</value> 
 </property> 
 <property> 
 <name>yarn.nodemanager.env-whitelist</name> 
  
<value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREP END_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value> 
 </property> 
</configuration>
~~~
~~~shell
ssh localhost
~~~
~~~shell
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa 
~~~
~~~shell
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
~~~
~~~shell
chmod 0600 ~/.ssh/authorized_keys 
~~~
~~~shell
hadoop-3.4.1/bin/hdfs namenode -format
~~~

Step 5 : Start hadoop
To start

~~~shell
start-all.sh
~~~
(Start NameNode daemon and DataNode daemon) 
localhost:9870

~~~shell
stop-all.sh
~~~
This is how you can install hadoop on your ubuntu operating system and start using on your system.


