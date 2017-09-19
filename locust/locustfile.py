import json
import random
import uuid
import time
import jwt
import urllib
import os
from locust import HttpLocust, TaskSet, task
from locust.exception import InterruptTaskSet, StopLocust
from locust.web import logger

an_endpoint_uri = "/some/uri/with/path/value/%i"

def queryGlobalMethodExample(self, value):
    headers = {
        "authId": self.locust.user_token,
        "Content-Type": "application/json"
    }
    response = self.client.get(
        an_endpoint_uri % value, name="/some/uri/with/path/value/[value]",
        headers=headers)

    if response.status_code == 200:
        return response.json()
    return None

class UserBehaviourTaskSet(TaskSet):
    @task(1)
    class ExampleOneTaskSet(TaskSet):
        min_wait = 60000
        max_wait = 60000

        endpoint_1_uri = "/some/uri/with/path/value/%i"

        def queryLocalMethodExample(self, value):
            headers = {
                "authId": self.locust.user_token,
                "Content-Type": "application/json"
            }
            response = self.client.get(
                self.endpoint_1_uri % value, name="/some/uri/with/path/value/[value]",
                headers=headers)

            if response.status_code == 200:
                return response.json()
            return None

        @task(0) # integer defines the weight of this task in relation to the other tasks
        def debug(self):            
            if not self.locust.user_token:
                logger.warn("Aborting task - unexpected user token")
                raise InterruptTaskSet(False)

        @task(1)
        def executeTestOne(self):

            result1 = queryGlobalMethodExample(self, "some-value")
            if result1 is not None:
                logger.debug("result2: %s" % result1)
            else:
                logger.warn("Error occurred... aborting task.")
                raise InterruptTaskSet(False)

        @task(1)
        def executeTestTwo(self):

            result1 = self.queryLocalMethodExample("some-value")
            if result1 is not None:
                logger.debug("result1: %s" % result1)
            else:
                logger.warn("Unrecoverable error occurred!")
                raise StopLocust("RIP...")

class UserBehaviourLocust(HttpLocust):

    task_set = UserBehaviourTaskSet
    user_token = None

    def __init__(self, *args, **kwargs):
        super(UserBehaviourLocust, self).__init__(*args, **kwargs)

        self.user_token = os.environ['EXT_TOKEN']
        if self.user_token is None:
            raise StopLocust("Invalid token. Seppuku!!!")

        logger.info("Locust [%s] is joining the swarm..." % self.user_id)
