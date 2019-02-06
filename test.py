from locust import HttpLocust, TaskSet, task
import json

def predict(l):
    headers = {'content-type': 'application/json'}
    data    = { "instances":[
                        {
                          "free sulfur dioxide":45.0,
                          "total sulfur dioxide":170.0,
                          "density":1.001,
                          "pH":3.0,
                          "sulphates":0.45,
                          "alcohol":8.8,
                          "fixed acidity":7.0,
                          "volatile acidity":0.27,
                          "citric acid":0.36,
                          "residual sugar":20.7,
                          "chlorides":0.045
                        }
                      ]}
    l.client.post("/predict", data=json.dumps(data), headers=headers)

class WebsiteTasks(TaskSet):
    tasks = {predict: 1}

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 9000