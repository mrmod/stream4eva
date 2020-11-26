Serves an infinite video stream from images or a TCP stream as HLS (HTTP Live Streaming) stream for a browser.


See `create_videos.sh` for usage

## Usage

```

# Create an infinite stream from generated images

./create_videos.sh

# Start NGinx to serve a simple webpage with a <video> tag
# pointed at the playlist/stream created byt the script above

./restart_nginx.sh

```

## Streaming from H264 over TCP

```
ssh raspberrypi 'nohup raspivid -v -n -fps 24 -t 0 -l -o tcp://0.0.0.0:8500 &'

./create_videos.sh LIVE

./restart_nginx.sh
```

Navigate to `http://localhost:9201` to watch your video stream
