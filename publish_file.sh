# publish video from file to topic '/camera/image_raw'

VID_FILE=$1    # absolute
FPS=${2:-5}

roslaunch video_stream_opencv camera.launch fps:=$FPS video_stream_provider:=$VID_FILE
