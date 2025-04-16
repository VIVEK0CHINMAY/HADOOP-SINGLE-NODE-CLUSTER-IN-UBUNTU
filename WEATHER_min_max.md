# 🌡️ WEATHER Cold Days Detection Using Hadoop Streaming

This guide walks through **finding the coldest days** from a weather dataset using **Hadoop Streaming** and custom **Python scripts**.

---

## 📂 Step 1: Create the Required Files

### 1️⃣ Create the `map_weather.py` File
```bash
nano map_weather.py
```

### 📝 Code for `mapweh.py`
```python
#!/usr/bin/env python2
import sys

for line in sys.stdin:
    if not line.strip():
        continue

    try:
        date = line[6:14]
        temp_min = float(line[47:53].strip())

        if temp_min < 15.0:
            # Format date to yyyy/mm/dd
            formatted_date = "%s/%s/%s" % (date[:4], date[4:6], date[6:])
            print "The Day is Cold Day :%s\t%.2f" % (formatted_date, temp_min)

    except:
        continue
```

### 🔐 Set Execute Permission
```bash
chmod +x map_weather.py
```

---

### 2️⃣ Create the `red_weather.py` File
```bash
nano red_weather.py
```

### 📝 Code for `redweh.py`
```python
#!/usr/bin/env python2
import sys

cold_days = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    key_value = line.split('\t', 1)
    if len(key_value) != 2:
        continue
    key, value = key_value
    try:
        temp = float(value)
        cold_days.append((key, temp))
    except:
        continue

# Sort by temperature (ascending)
cold_days.sort(key=lambda x: x[1])

# Print top 10 coldest days
for entry in cold_days[:10]:
    print "%s\t%.2f" % (entry[0], entry[1])
```

### 🔐 Set Execute Permission
```bash
chmod +x red_weather.py
```

---

## 📤 Step 2: Prepare Input Data

### 🗂️ Create and Upload Input File
```bash
hdfs dfs -mkdir /weather
hdfs dfs -copyFromLocal /home/vivan/weather_datset.txt /weather
```

---

## 🚀 Step 3: Run Hadoop Streaming Job

### 💻 Execute MapReduce Job with Python Scripts
```bash
hadoop jar /home/vivan/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
    -input /weather/weather_datset.txt \
    -output /weather/output \
    -mapper "python2 /home/vivan/map_weather.py" \
    -reducer "python2 /home/vivan/red_weather.py"
```

> ⚠️ Make sure all paths are accurate and scripts have execution permission.

---

## 📥 Step 4: View Output Results

### 📄 Display Top 10 Coldest Days
```bash
hdfs dfs -cat /weather/output/part-00000
```

---

## ❄️ Done!
You’ve successfully extracted the **coldest days** from weather data using Hadoop Streaming! 🧊📉

