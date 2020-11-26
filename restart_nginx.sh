NAME="stream4eva"

docker kill $NAME

docker run \
  -d \
  --name $NAME \
  --rm \
  -p 9100:80 \
  -p 9201:9201 \
  -v $(pwd)/videos:/videos \
  -v $(pwd)/hls_streaming.conf:/etc/nginx/conf.d/hls_streaming.conf \
  nginx

cp index.html videos/
