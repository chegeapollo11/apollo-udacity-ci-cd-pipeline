import time

from locust import HttpUser, task, between

class MLUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def test_predict(self):
        payload = {"CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}}
        self.client.post("/predict", json = payload)
