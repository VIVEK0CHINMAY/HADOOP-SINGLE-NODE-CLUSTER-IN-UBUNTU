# 📊 Word Count Using Hadoop Streaming

This guide walks you through the **complete setup of a Word Count** MapReduce job using **Hadoop Streaming** and **Python scripts**.

---

## 📂 Step 1: Create the Required Files

### 1️⃣ Create the `mapper.py` File
```bash
cd Documents/
touch mapper.py
```

### 📝 Code for `mapper.py`
```python
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))
```

### 🔐 Set Execute Permission
```bash
chmod +x mapper.py
```

---

### 2️⃣ Create the `reducer.py` File
```bash
touch reducer.py
```

### 📝 Code for `reducer.py`
```python
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

if current_word == word:
    print('%s\t%s' % (current_word, current_count))
```

### 🔐 Set Execute Permission
```bash
chmod +x reducer.py
```

---

## 📤 Step 2: Prepare Input Data

### 🗂️ Create and Upload Input File
```bash
hdfs dfs -mkdir /wordcount
hdfs dfs -copyFromLocal /home/vivan/input.txt /wordcount
```

---

## 🚀 Step 3: Run Hadoop Streaming Job

### 💻 Execute MapReduce Job with Python Scripts
```bash
hadoop jar /home/vivan/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
    -input /wordcount/input.txt \
    -output /wordcount/output \
    -mapper "/home/vivan/mapper.py" \
    -reducer "/home/vivan/reducer.py"
```

> ⚠️ Ensure the path to the Hadoop Streaming JAR file and your Python scripts are correct.

---

## 📥 Step 4: View Output Results

### 📄 Display Word Count Output
```bash
hdfs dfs -cat /wordcount/output/part-00000
```

---

## ✅ You're Done!
You've now successfully implemented Word Count using Hadoop Streaming with custom Python scripts. 🎉

Need to try with other datasets or expand it? Just ask!

