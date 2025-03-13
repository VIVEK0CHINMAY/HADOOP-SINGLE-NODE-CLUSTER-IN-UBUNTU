# 🚀 Hadoop HDFS Commands Cheat Sheet

Welcome to the **Hadoop HDFS Commands** README! This guide provides essential commands to interact with the Hadoop Distributed File System (HDFS). 🔥

## 🔧 General Setup

### Start Hadoop Services - `start-all.sh`
Starts all Hadoop services.

#### Syntax:
```bash
start-all.sh
```

### Check Running Hadoop Services - `jps`
Lists running Java processes to verify Hadoop services.

#### Syntax:
```bash
jps
```

---

## 📂 HDFS Commands

### 📜 List Files and Directories - `ls`
Displays the list of files and directories stored in HDFS.

#### Syntax:
```bash
bin/hdfs dfs -ls <path>
```
Example:
```bash
bin/hdfs dfs -ls /
```

### 📁 Create a Directory - `mkdir`
Creates a new directory inside HDFS.

#### Syntax:
```bash
bin/hdfs dfs -mkdir <folder_name>
```
Example:
```bash
bin/hdfs dfs -mkdir /vivan
```

### 📝 Create an Empty File - `touchz`
Creates an empty file inside HDFS.

#### Syntax:
```bash
bin/hdfs dfs -touchz <file_path>
```
Example:
```bash
bin/hdfs dfs -touchz /vivan/myfile.txt
```

### ⬆️ Copy Files from Local to HDFS - `copyFromLocal`
Copies a file from the local filesystem to HDFS.

#### Syntax:
```bash
bin/hdfs dfs -copyFromLocal <local_file_path> <hdfs_path>
```
Example:
```bash
bin/hdfs dfs -copyFromLocal /home/vivan/input.txt /vivan
```

### 📖 Print File Contents - `cat`
Displays the contents of a file stored in HDFS.

#### Syntax:
```bash
bin/hdfs dfs -cat <path>
```
Example:
```bash
bin/hdfs dfs -cat /vivan/input.txt
```

### ⬇️ Copy Files from HDFS to Local - `copyToLocal`
Copies files from HDFS to the local filesystem.

#### Syntax:
```bash
bin/hdfs dfs -copyToLocal <hdfs_path> <local_file_path>
```
Example:
```bash
bin/hdfs dfs -copyToLocal /vivan /home/vivan
```

### ✂️ Move File from Local to HDFS - `moveFromLocal`
Moves a file from the local filesystem to HDFS.

#### Syntax:
```bash
bin/hdfs dfs -moveFromLocal <local_path> <hdfs_path>
```
Example:
```bash
bin/hdfs dfs -moveFromLocal /home/vivan/input2.txt /vivan
```

### 📌 Copy Files within HDFS - `cp`
Copies files from one HDFS location to another.

#### Syntax:
```bash
bin/hdfs dfs -cp <source> <destination>
```
Example:
```bash
bin/hdfs dfs -cp /vivan /vivan_copied
```

### 🔀 Move Files within HDFS - `mv`
Moves files from one HDFS location to another.

#### Syntax:
```bash
bin/hdfs dfs -mv <source> <destination>
```
Example:
```bash
bin/hdfs dfs -mv /vivan/input2.txt /vivan_copied
```

### 🗑️ Recursively Delete Files/Directories - `rmr`
Deletes files or directories recursively from HDFS.

#### Syntax:
```bash
bin/hdfs dfs -rmr <filename/directory>
```
Example:
```bash
bin/hdfs dfs -rmr /vivan_copied
```

### 📏 Display File Sizes - `du`
Shows the size of each file in the specified HDFS directory.

#### Syntax:
```bash
bin/hdfs dfs -du <dirName>
```
Example:
```bash
bin/hdfs dfs -du /vivan
```

### 📊 Show Total Directory/File Size - `dus`
Displays the total size of a file or directory in HDFS.

#### Syntax:
```bash
bin/hdfs dfs -dus <dirName>
```
Example:
```bash
bin/hdfs dfs -dus /vivan
```

### 📊 View File/Directory Statistics - `stat`
Provides metadata information about a file or directory in HDFS.

#### Syntax:
```bash
bin/hdfs dfs -stat <path>
```
Example:
```bash
bin/hdfs dfs -stat /vivan
```

### 🔄 Change File Replication Factor - `setrep`
Modifies the replication factor of a file in HDFS.

#### Syntax:
```bash
bin/hdfs dfs -setrep -R -w <replication_factor> <path>
```
Example:
```bash
bin/hdfs dfs -setrep -R -w 6 /vivan/input.txt
```

---

## 🎯 Additional Notes

✅ These commands help you efficiently manage files in HDFS. There are many more commands available!

📖 To see the full list, run:
```bash
bin/hdfs dfs
```

Happy Hadooping! 🎉

