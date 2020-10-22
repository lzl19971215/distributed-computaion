#!/bin/bash

PWD=$(cd $(dirname $0); pwd)

cd $PWD 1> /dev/null 2>&1
TASKNAME=feature_selection

HADOOP_INPUT_DIR=/user/devel/2020210983Liziliang/used_cars_100.csv
HADOOP_OUTPUT_DIR=/user/devel/2020210983Liziliang/$TASKNAME
echo $HADOOP_INPUT_DIR
echo $HADOOP_OUTPUT_DIR
hadoop fs -rm -r $HADOOP_OUTPUT_DIR
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-file $PWD/feature_selection_mapper1.py  $PWD/feature_selection_reducer.py \
-output ${HADOOP_OUTPUT_DIR} \
-input ${HADOOP_INPUT_DIR} \
-mapper "python3 feature_selection_mapper1.py" \
-reducer "python3 feature_selection_reducer.py" 
if [ $? -ne 0 ]; then
    echo 'error'
    exit 1
fi
hadoop fs -touchz ${HADOOP_OUTPUT_DIR}/done
exit 0

