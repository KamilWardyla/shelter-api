from locust import HttpUser, task, between


class MethodGetTest(HttpUser):
    wait_time = between(0, 1.5)

    @task
    def get_animal(self):
        with self.client.get("/animals", catch_response=True) as response:
            if response.status_code != 200:
                response.failure('Got wrong response')
