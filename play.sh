# Publish video from bag file to topic '/cam/image_raw' or '/cam/image_raw'.

BAG_FILE=$1    # Path to bag file.

if [ $# != 1 ]; then
    echo usage: ./play.sh PATH_TO_BAG_FILE
    exit
fi

rosbag play $BAG_FILE
