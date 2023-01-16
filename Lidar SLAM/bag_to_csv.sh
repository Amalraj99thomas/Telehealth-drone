#!/bin/bash
# My first script
#$1 is the name of the .bag file, $2 is the name of the topic and $3 is the name of the .csv file
#example ./bag_to_csv.sh imu_data.bag /imu/data_raw imu_data_raw.csv
rostopic echo -b $1 -p $2 > $3