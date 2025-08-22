# Publish video from RTSP stream to topic '/cam/image_raw'.

URI=$1    # Schemeless URI of video stream.

if [ $# != 1 ]; then
    echo usage: ./publish_stream.sh URI
    exit
fi

roslaunch gstreamer_cv rtsp_single_stream.launch rtsp_url:=$URI
