# 🚀 HADOOP SINGLE NODE CLUSTER SETUP IN UBUNTU

## ✅ Step 1: Add a User in Ubuntu 👤
- Login as a user and open the terminal.
- Paste the below code and replace `<username>` with your own name:
  
  ```shell
  sudo adduser <username>
  ```
  
- Provide a username, set a password, and confirm by typing 'yes'.

---

## ✅ Step 2: Log in to Your Account 🔑
- Click on the power button and switch users.
- Select the user you created and log in.

---

## ✅ Step 3: Install Java JDK 11 ☕
First, check the Java version installed on your system:
  
```shell
java --version
```
  
If the output shows Java 11, proceed to Step 4. Otherwise, refer to the [Java Installation](java_installation) README file.

---

## ✅ Step 4: Download the Hadoop Tar File 📥
Run the following command to download the Hadoop tar file:
  
```shell
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz
```
  
Extract the tar file:
  
```shell
tar -zxvf ~/hadoop-3.4.1.tar.gz
```

---

## ✅ Step 5: Configure Environment Variables 🛠️
Open the `.bashrc` file using:
  
```shell
nano ~/.bashrc
```
  
Paste the following inside the script:
  
```shell
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
```
  
Save and exit: Press `Ctrl+X`, then `Y`, and hit `Enter`.
  
Apply the changes:
  
```shell
source ~/.bashrc
```

---

## ✅ Step 6: Hadoop Site Setup 🏗️
Navigate to the Hadoop folder:
  
```shell
cd hadoop-3.4.1/etc/hadoop
```
  
Open `hadoop-env.sh`:
  
```shell
nano hadoop-env.sh
```
  
Find `JAVA_HOME` and add the following line:
  
```shell
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```
  
Save and exit.

---

## ✅ Step 7: Configure `core-site.xml` 🛠️
  
```shell
nano core-site.xml
```
  
Replace the configuration with:
  
```xml
<configuration>
 <property>
   <name>fs.defaultFS</name>
   <value>hdfs://localhost:9000</value>
 </property>
</configuration>
```
  
Save and exit.

---

## ✅ Step 8: Configure `hdfs-site.xml` 🗄️
  
```shell
nano hdfs-site.xml
```
  
Replace the configuration with:
  
```xml
<configuration>
 <property>
   <name>dfs.replication</name>
   <value>1</value>
 </property>
</configuration>
```
  
Save and exit.

---

## ✅ Step 9: Configure `mapred-site.xml` 🛠️
  
```shell
nano mapred-site.xml
```
  
Replace the configuration with:
  
```xml
<configuration>
 <property>
   <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>
</configuration>
```
  
Save and exit.

---

## ✅ Step 10: Configure `yarn-site.xml` 🎯
  
```shell
nano yarn-site.xml
```
  
Replace the configuration with:
  
```xml
<configuration>
 <property>
   <name>yarn.nodemanager.aux-services</name>
   <value>mapreduce_shuffle</value>
 </property>
</configuration>
```
  
Save and exit.

---

## ✅ Step 11: Start SSH Localhost 🔑
  
```shell
ssh localhost
```
  
This establishes an SSH connection to your machine.

---

## ✅ Step 12: Generate SSH Keys 🔑
  
```shell
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
```
  
Add the public key to authorized keys:
  
```shell
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```
  
Format the Hadoop NameNode:
  
```shell
hadoop-3.4.1/bin/hdfs namenode -format
```

---

## ✅ Step 13: Start Hadoop 🚀
  
```shell
start-all.sh
```
  
This starts the NameNode and DataNode daemons.

---

## ✅ Step 14: Check Running Services 📊
  
```shell
jps
```
  
This will show all running Hadoop services.

🔗 Open the following web interfaces:
- [NameNode UI](http://localhost:9870)
- [DataNode UI](http://localhost:9864)
- [YARN Resource Manager](http://localhost:8088)

---

## ✅ Step 15: Stop Hadoop ❌
  
```shell
stop-all.sh
```
  
This stops all running Hadoop services.

🎉 **Congratulations!** You have successfully installed and configured Hadoop on your Ubuntu system. 🚀

