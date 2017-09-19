#!/bin/bash

docker run \
	-p 8089:8089 \	
	-e EXT_TOKEN="auth-id-token-value" \
	-e LOCUST_MODE=standalone \
	-e TARGET_URL=http://172.17.0.1:8080 \
    -v /path/of/you/locust/work/FOLDER/with/locustfile/on/it:/locust \
    --name locust-standalone \
	-d locust-standalone