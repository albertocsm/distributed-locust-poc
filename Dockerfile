FROM hakobera/locust
# https://github.com/hakobera/docker-locust

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y libffi-dev && apt-get clean
RUN easy_install pip 
RUN pip install cryptography PyJWT paho-mqtt


ADD ./locust /locust
ENV SCENARIO_FILE /locust/locustfile.py