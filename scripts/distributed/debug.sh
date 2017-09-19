#!/bin/bash
bash destroy.sh
bash start.sh
docker logs -f locust-master
