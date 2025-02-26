# HADOOP-SINGLE-NODE-CLUSTER-IN-UBUNTU

### Step 1 : Add user in ubuntu 
- Login to asas user and open terminal
- paste the below code and replace the <username> with your own name
~~~shell
sudo adduser username
~~~
- give user name again and set pass word and type yes

### Step 2 : Loging into your Account
- Now click on power button and switch user
- Select the user that you created now and login to the user

### Step 3 : Install java jdk 11
First check for java version in your system 
~~~shell
java --version
~~~
If the output is 11 then go to Step 4
or check out [Java_installation](java_installation) readme file 

### Step 4 : Download the hadoop tar file 
Run the below command to download ther hadoop tar file 
~~~shell
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz
~~~
(Extract the tar file)
~~~shell
tar -zxvf ~/hadoop-3.4.1.tar.gz 
~~~

### Step 5 : Add this configuration on you bash file

Now just open .bashrc file and paste these commands.
to open use the below command 
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
press Ctrl+X , Ctrl+Y press enter

now source the code so that the changes is made
run this after pasting the above command
~~~shell
source ~/.bashrc
~~~
### Step 6 : Hadoop site setup

Enter to hadoop folder 
run:
~~~shell
cd hadoop-3.4.1/etc/hadoop
~~~
now open hadoop-env.sh
~~~shell
nano hadoop-env.sh
~~~
find for JAVA_HOME in script and paste the below line 
~~~shell
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64 
~~~
press Ctrl+X , Ctrl+Y press enter

### Step 7 : Add this file in core-site.xml

Now add this configuration in core-site.xml file.
~~~shell
nano core-site.xml
~~~
paste the below script in the place of configuration
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
press Ctrl+X , Ctrl+Y press enter

### Step 8 : Add this file in hdfs-site.xml
Now add this configuration in hdfs-site.xml file.
~~~shell
nano hdfs-site.xml
~~~
paste the below script in the place of configuration
~~~ shell
<configuration> 
 <property> 
 <name>dfs.replication</name> 
 <value>1</value> 
 </property> 
</configuration>
~~~
press Ctrl+X , Ctrl+Y press enter

### Step 9: Add this file in mapred-site.xml
Now add this configuration in mapred-site.xml file.
~~~shell
nano mapred-site.xml
~~~
paste the below script in the place of configuration
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
press Ctrl+X , Ctrl+Y press enter

### Step 10: Add this file in yarn-site.xml
Now add this configuration in yarn-site.xml file.
~~~shell
nano yarn-site.xml
~~~
paste the below script in the place of configuration
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
press Ctrl+X , Ctrl+Y press enter

### Step 11: start the localhost
~~~shell
ssh localhost
~~~
it attempts to establish an SSH (Secure Shell) connection to your own machine (localhost).

### Step 12: Generating authorized_keys 
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
It initializes the Hadoop file system by deleting old metadata and preparing a fresh NameNode storage.

### Step 13 : Start hadoop
To start

~~~shell
start-all.sh
~~~
(Start NameNode daemon and DataNode daemon) 

### Step 14: Check the services running
Run:
~~~shell
jps
~~~
it will show the services running 

Now open these sites
The NameNode user interface provides a comprehensive overview of the entire cluster
```
[(http://localhost:9870](http://localhost:9870)
```
The default port 9864 is used to access individual DataNodes directly from your browser:
[http://localhost:9864](http://localhost:9864)
The YARN Resource Manager is accessible on port 8088:
[http://localhost:8088](http://localhost:8088)

### Step 15 : Stop hadoop
~~~shell
stop-all.sh
~~~
This is how you can install hadoop on your ubuntu operating system and start using on your system.


