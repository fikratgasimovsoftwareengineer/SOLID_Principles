from concurrent.futures import ThreadPoolExecutor
import time
import asyncio


def log_message(message):
    print(f"{message} at P{time.ctime()}")
    
def send_notification(user):
    print(f"Notifying {user} at {time.ctime()}")
    
def run():
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        print("Submitting tasks to the thread pool...")
        executor.submit(log_message, "Task_1")
        executor.submit(send_notification, "User_1")
        print(f"Active threads: {executor._threads}")
        
    print("All tasks completed.")
    
if __name__ == "__main__":
    run()