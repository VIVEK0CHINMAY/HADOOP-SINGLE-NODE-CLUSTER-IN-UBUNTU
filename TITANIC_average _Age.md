# 🚢 Titanic Average Age by Gender using Hadoop Streaming

This guide walks you through the **complete setup of a Hadoop Streaming job** to calculate **average age by gender** from Titanic dataset using **Python scripts**.

---

## 📂 Step 1: Create the Required Files

### 1️⃣ Create the `map_titanic.py` File
```bash
nano map_titanic.py
```

### 📝 Code for `maptit.py`
```python
#!/usr/bin/env python2
import sys
import csv

def read_input(file):
    for line in file:
        yield list(csv.reader([line]))[0]

first_line = True
for columns in read_input(sys.stdin):
    if first_line:
        first_line = False  # skip header if needed
        continue
    try:
        gender = columns[4].strip().lower()
        age = columns[5].strip()
        if gender in ['male', 'female'] and age != '':
            print '%s\t%s' % (gender, age)
    except:
        continue
```

### 🔐 Set Execute Permission
```bash
chmod +x map_titanic.py
```

---

### 2️⃣ Create the `redtit.py` File
```bash
nano red_titanic.py
```

### 📝 Code for `redtit.py`
```python
#!/usr/bin/env python2
import sys

current_gender = None
total_age = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    gender, age = line.split('\t', 1)
    try:
        age = float(age)
    except ValueError:
        continue

    if current_gender == gender:
        total_age += age
        count += 1
    else:
        if current_gender:
            avg = total_age / count if count > 0 else 0
            print '%s\t%.2f' % (current_gender, avg)
        current_gender = gender
        total_age = age
        count = 1

# Don't forget the last key
if current_gender:
    avg = total_age / count if count > 0 else 0
    print '%s\t%.2f' % (current_gender, avg)
```

### 🔐 Set Execute Permission
```bash
chmod +x red_titanic.py
```

---

## 📤 Step 2: Prepare Input Data

### 🗂️ Create and Upload Titanic Input File
```bash
hdfs dfs -mkdir /titanic
hdfs dfs -copyFromLocal /home/vivan/titanic_data.txt /titanic
```

---

## 🚀 Step 3: Run Hadoop Streaming Job

### 💻 Execute Hadoop Job with Titanic Scripts
```bash
hadoop jar /home/vivan/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
    -input /titanic/titanic_data.txt \
    -output /titanic/output \
    -mapper "python2 /home/vivan/map_titanic.py" \
    -reducer "python2 /home/vivan/red_titanic.py"
```

---

## 📥 Step 4: View Output Results

### 📄 Display Average Age by Gender
```bash
hdfs dfs -cat /titanic/output/part-00000
```

---

## ✅ You're Done!
You've now successfully calculated the **average age of male and female passengers** from the Titanic dataset using Hadoop Streaming. 🌊

Want to explore more with Titanic data? Feel free to ask!

