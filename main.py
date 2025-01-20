import requests
from threading import Thread
import time

url = "http://localhost:4200/"

num_requests = 10000000
threads = []

def send_request(request_id):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        duration = time.time() - start_time
        print(f"Request {request_id} | Status: {response.status_code} | Time: {duration:.2f}s")
    except Exception as e:
        print(f"Request error {request_id}: {e}")

for i in range(num_requests):
    thread = Thread(target=send_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Finished test!")