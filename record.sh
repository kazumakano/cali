# Subscribe video from topic '/cam/image_raw' and '/cam/image_raw' and save to bag.
# Press Ctrl + C to exit.

CAM_NAME=$1      # Camera name.
RESULT_DIR=$2    # Path to result directory.

mkdir --parents $RESULT_DIR/$CAM_NAME/
rosbag record rosout /camera/image_raw /cam/image_raw --output-name=$RESULT_DIR/$CAM_NAME/video
