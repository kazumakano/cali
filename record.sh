# subscribe video from topic '/cam/image_raw' and '/cam/image_raw' and save to bag
# press Ctrl + C to exit

BAG_DIR=$1     # path to bag directory
CAM_NAME=$2    # camera name

rosbag record rosout /camera/image_raw /cam/image_raw --output-name=${BAG_DIR%/}/$CAM_NAME
