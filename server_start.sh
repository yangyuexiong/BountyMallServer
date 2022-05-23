#!/bin/bash

BountyMallUUID=`docker ps | grep bm_server | awk '{print $1}'`;

if [ $BountyMallUUID ]; then
  docker stop $BountyMallUUID;
  echo "stop success";
  docker rm $BountyMallUUID;
  echo "rm success";
fi

echo y | docker system prune
docker build -t 'bm_server' .
echo "build success"
#docker run -v /srv/test_reports:/srv/BountyMallServer/app/static/report -d --network host --name bm_server bm_server
docker run -v /srv/BountyMallServer/app/static/report:/srv/BountyMallServer/app/static/report -v /srv/UiRecorderProject:/srv/BountyMallServer/app/static/UiRecorderProject -d --network host --name bm_server bm_server
# docker run -d --network host --name bm_server bm_server
# docker run -d -p 5000:5000 --name bm_server bm_server
echo "run success"

# cat /proc/sys/net/core/somaxconn
# echo  65535  >  /proc/sys/net/core/somaxconn