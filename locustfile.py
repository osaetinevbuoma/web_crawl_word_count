import time

from locust import HttpUser, between, task


class CrawlerServiceLoadTestUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def healthcheck(self):
        self.client.get("/health")

    @task(15)
    def word_occurrence(self):
        urls = ["https://www.bbc.co.uk", "https://www.cnn.com", "https://www.google.com",
                "https://www.amazon.co.uk", "https://www.yahoo.com", "https://www.facebook.com",
                "https://www.invaliddomainname.co.uk", "https://www.ebay.co.uk",
                "https://www.paypal.com", "https://www.tesla.com"]

        for url in urls:
            self.client.get(f"/count-words?url={url}")
            time.sleep(1)
