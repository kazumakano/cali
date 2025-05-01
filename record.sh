# Subscribe video from topic '/cam/image_raw' and '/cam/image_raw' and save to bag.
# Press Ctrl + C to exit.

BAG_DIR=$1     # Path to bag directory.
CAM_NAME=$2    # Camera name.

rosbag record rosout /camera/image_raw /cam/image_raw --output-name=$BAG_DIR/$CAM_NAME
