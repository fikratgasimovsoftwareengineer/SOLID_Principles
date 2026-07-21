import time
import threading
import asyncio
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import os
thread_task_count = defaultdict(int)
thread_names = set()

all_threads = min(32, os.cpu_count()+4)
def get_status_code(url: str, task_id: int) -> int:
    import requests
    thread_name = threading.current_thread().name
    thread_task_count[thread_name] += 1
    thread_names.add(thread_name)
    response = requests.get(url)
    return response.status_code

async def main():
    start = time.time()
    urls = ['https://www.example.com' for _ in range(1000)]

    # imposta executor PRIMA di creare i task
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(
        max_workers=all_threads,           # solo 10 thread
        thread_name_prefix="mio_worker"  # nome custom!
    )
    loop.set_default_executor(executor)

    tasks = [
        asyncio.to_thread(get_status_code, url, i)
        for i, url in enumerate(urls)
    ]

    results = await asyncio.gather(*tasks)

    end = time.time()

    print("=" * 60)
    print(f"Thread UNICI usati: {len(thread_names)}")
    print(f"Distribuzione task per thread:")
    for name in sorted(thread_names):
        print(f"  {name:40s} -> {thread_task_count[name]:4d} task")
    print(f"Tempo totale: {end-start:.2f}s")
    print(f"Task medi per thread: {len(urls)/len(thread_names):.1f}")

asyncio.run(main())