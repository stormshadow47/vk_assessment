import time
import threading
from collections import deque

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests = {}
        self.lock = threading.Lock()
    
    def allow_request(self, user_id):
        current_time = time.time()
        
        with self.lock:
            if user_id not in self.user_requests:
                self.user_requests[user_id] = deque()
            
            request_queue = self.user_requests[user_id]

            while request_queue and request_queue[0] < current_time - self.time_window:
                request_queue.popleft()

            if len(request_queue) < self.max_requests:
                request_queue.append(current_time)
                return True
            else:
                return False

def user_requests(user_id, rate_limiter, num_requests, wait_time_between_requests):
    for i in range(num_requests):
        if rate_limiter.allow_request(user_id):
            print(f"User {user_id}: Request {i + 1} is allowed.")
        else:
            print(f"User {user_id}: Request {i + 1} is denied.")
        time.sleep(wait_time_between_requests)

rate_limiter = RateLimiter(max_requests=5, time_window=60)

def test_rate_limiter_concurrent():
    user_1_thread = threading.Thread(target=user_requests, args=('user_1', rate_limiter, 7, 1))

    user_2_thread = threading.Thread(target=user_requests, args=('user_2', rate_limiter, 5, 0.5))
    
    user_1_thread.start()
    user_2_thread.start()

    user_1_thread.join()
    user_2_thread.join()


test_rate_limiter_concurrent()
