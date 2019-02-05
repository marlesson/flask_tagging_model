from locust import HttpLocust, TaskSet, task

def predict(l):
    l.client.post("/predict", {"username":"ellen_key", "password":"education"})

class WebsiteTasks(TaskSet):
    tasks = {predict: 1}

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 9000