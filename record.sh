# subscribe video from topic '/cam/image_raw' and '/cam/image_raw' and save to bag
# press Ctrl + C to exit

BAG_DIR=$1
CAM_NAME=$2

rosbag record rosout /camera/image_raw /cam/image_raw -O ${BAG_DIR%/}/$CAM_NAME
