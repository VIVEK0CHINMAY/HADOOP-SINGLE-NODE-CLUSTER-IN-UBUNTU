hdfs dfs -mkdir /titanic
hdfs dfs -copyFromLocal /home/vivan/titanic_data.txt /titanic
hadoop jar /home/vivan/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
    -input /titanic/titanic_data.txt \
    -output /titanic/output \
    -mapper "python2 /home/vivan/maptit.py" \
    -reducer "python2 /home/vivan/redtit.py"
chmod +x maptit.py redtit.py
hdfs dfs -cat /titanic/output/part-00000

weather_datset
chmod +x mapweh.py redweh.py
hdfs dfs -mkdir /weather
hdfs dfs -copyFromLocal /home/vivan/weather_datset.txt /weather
hadoop jar /home/vivan/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
    -input /weather/weather_datset.txt \
    -output /weather/output \
    -mapper "python2 /home/vivan/mapweh.py" \
    -reducer "python2 /home/vivan/redweh.py"
hdfs dfs -cat /weather/output/part-00000
