#!bash
docker kill locust-master
docker rm -v locust-master

docker kill locust-slave-1
docker rm -v locust-slave-1

docker kill locust-slave-2
docker rm -v locust-slave-2