import time
import threading
from collections import defaultdict
import asyncio

# --- TRACCIAMENTO ---
thread_task_count = defaultdict(int)
thread_names = set()

def get_status_code(url: str, task_id: int) -> int:
    import requests
    thread_name = threading.current_thread().name
    
    # Traccia
    thread_task_count[thread_name] += 1
    thread_names.add(thread_name)
    
    response = requests.get(url)
    return response.status_code

async def main():
    start = time.time()
    urls = ['https://www.example.com' for _ in range(1000)]
    
    tasks = [
        asyncio.to_thread(get_status_code, url, i) 
        for i, url in enumerate(urls)
    ]
    
    results = await asyncio.gather(*tasks)
    
    end = time.time()
    
    # --- REPORT ---
    print("=" * 60)
    print("ANALISI THREAD")
    print("=" * 60)
    print(f"Task totali: {len(urls)}")
    print(f"Thread UNICI usati: {len(thread_names)}")
    print(f"Nomi thread: {sorted(thread_names)}")
    print(f"\nDistribuzione task per thread:")
    for name in sorted(thread_names):
        print(f"  {name:30s} -> {thread_task_count[name]:4d} task")
    print(f"\nTempo totale: {end-start:.2f}s")
    print(f"Task medi per thread: {len(urls)/len(thread_names):.1f}")

asyncio.run(main())