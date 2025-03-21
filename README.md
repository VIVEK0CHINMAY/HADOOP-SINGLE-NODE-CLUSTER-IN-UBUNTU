# Hadoop Streaming Word Count with Stopword Filtering

This project demonstrates a simple Hadoop Streaming job to perform a word count while filtering out common stop words using Python scripts (`map.py` and `reduce.py`). The process involves running a MapReduce job using `hadoop-streaming.jar`.

---

## Prerequisites

- Hadoop installed and configured
- Python 2 installed (for compatibility with Hadoop Streaming)
- HDFS up and running

---

## Steps to Run the MapReduce Job

### 1. Create and Write the Mapper Script (`map.py`)

Create the `map.py` file and paste the following code:

```python
#!/usr/bin/env python2

import sys

# Define stop words directly in the code
STOP_WORDS = set([
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "could", "did", "do", "does", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "her", "here", "hers", "him", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "let", "me", "more", "most", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "should", "so", "some", "such", "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "you", "your", "yours", "yourself", "yourselves"
])

# Mapper function
def mapper():
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            if word.lower() not in STOP_WORDS:
                print("{}\t{}".format(word.lower(), 1))

if __name__ == "__main__":
    mapper()
```

Make the script executable:
```sh
chmod +x map.py
```

---

### 2. Create and Write the Reducer Script (`reduce.py`)

Create the `reduce.py` file and paste the following code:

```python
#!/usr/bin/env python2

import sys
from collections import defaultdict

# Reducer function
def reducer():
    word_count = defaultdict(int)

    for line in sys.stdin:
        word, count = line.strip().split("\t")
        word_count[word] += int(count)

    for word, count in word_count.items():
        print("{}\t{}".format(word, count))

if __name__ == "__main__":
    reducer()
```

Make the script executable:
```sh
chmod +x reduce.py
```

---

### 3. Prepare Input Data

Ensure you have an input text file (`input.txt`) with sample text to be processed.

Move the input file to HDFS:
```sh
hdfs dfs -mkdir /stopword
hdfs dfs -copyFromLocal /home/vivan/input.txt /stopword
```

---

### 4. Run the Hadoop Streaming Job

Execute the following command to run the Hadoop Streaming job:

```sh
hadoop jar /home/vivan/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
    -input /stopword/input.txt \
    -output /stopword/output \
    -mapper "python2 /home/vivan/map.py" \
    -reducer "python2 /home/vivan/reduce.py"
```

---

### 5. View the Output

Once the job completes, view the output using:
```sh
hdfs dfs -cat /stopword/output/part-00000
```

This should display word counts while filtering out stop words.

---

## Summary

- `map.py` filters out common stop words and emits word counts.
- `reduce.py` aggregates the word counts.
- The job is executed using Hadoop Streaming.
- The final output shows the word count after stop words are removed.

This project is useful for basic text processing tasks such as data cleaning and analysis using Hadoop MapReduce.

