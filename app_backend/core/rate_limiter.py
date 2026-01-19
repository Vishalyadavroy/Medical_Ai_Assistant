import time 

REQUEST_LIMIT = 5
WINDOW = 60 

user_requests = {}

def check_rate_limit(user_id:str):
    now = time.time()
    requests = user_requests.get(user_id,[])

    requests = [t for t in requests if now - t < WINDOW]

    if len(requests) >= REQUEST_LIMIT:
        return False
    
    requests.append(now)
    user_requests[user_id] = requests
    return True