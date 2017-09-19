#!/bin/bash

docker run \
	-p 8089:8089 \
	-p 5557:5557 \
	-p 5558:5558 \	
	-e EXT_TOKEN="auth-id-token-value" \
	-e LOCUST_MODE=master \
	-e TARGET_URL=http://172.17.0.1:8080 \
    -v /path/of/you/locust/work/FOLDER/with/locustfile/on/it:/locust \
    --name locust-master \
	-d locust-distributed

docker run \	
	-e EXT_TOKEN="auth-id-token-value" \
	-e LOCUST_MODE=slave \
	-e MASTER_HOST=172.17.0.1 \
	-e TARGET_URL=http://172.17.0.1:8080 \
    -v /path/of/you/locust/work/FOLDER/with/locustfile/on/it:/locust \
    --name locust-slave-1 \
	-d locust-distributed

docker run \
	-e EXT_TOKEN="auth-id-token-value" \
	-e LOCUST_MODE=slave \
	-e MASTER_HOST=172.17.0.1 \
	-e TARGET_URL=http://172.17.0.1:8080 \
    -v /path/of/you/locust/work/FOLDER/with/locustfile/on/it:/locust \
    --name locust-slave-2 \
	-d locust-distributed