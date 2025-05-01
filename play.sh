# Publish video from bag file to topic '/cam/image_raw' or '/cam/image_raw'.

BAG_FILE=$1    # Path to bag file.

rosbag play $BAG_FILE
