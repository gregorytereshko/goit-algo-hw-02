import queue
import time
import random

def generate_request(q, request_id):
    request = f"Request {request_id}"
    print(f"Generating new request: {request}")
    q.put(request)

def process_request(q):
    if not q.empty():
        request = q.get()
        print(f"Processing request: {request}")
    else:
        print("Queue is empty, no requests to process.")

def main():
    request_queue = queue.Queue()
    request_id = 0
    try:
        while True:
            # Генерувати нові заявки кожні 2 секунди
            generate_request(request_queue, request_id)
            request_id += 1
            time.sleep(2)

            if random.randint(1, 2) == 1:  # Імітація інтервалу обробки
                process_request(request_queue)

            time.sleep(1)  # Затримка між ітераціями головного циклу
    except KeyboardInterrupt:
        print("\nProgram terminated by user. Exiting...")

if __name__ == "__main__":
    main()
