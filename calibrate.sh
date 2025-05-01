# Conduct calibration with bag file.

BOARD_FILE=$1                # Path to board file.
CAM_NAME=$2                  # Camera name.
RESULT_DIR=$3                # Path to result directory.
FILE_OR_STREAM=${4:-file}    # Whether file or stream. Default is file.

if [ $FILE_OR_STREAM = file ]; then
    rosrun kalibr tartan_calibrate --bag $RESULT_DIR/$CAM_NAME/video.bag --target $BOARD_FILE --topics /camera/image_raw --models ds-none --save_dir $RESULT_DIR/$CAM_NAME/
elif [ $FILE_OR_STREAM = stream ]; then
    rosrun kalibr tartan_calibrate --bag $RESULT_DIR/$CAM_NAME/video.bag --target $BOARD_FILE --topics /cam/image_raw --models ds-none --save_dir $RESULT_DIR/$CAM_NAME/
fi
