import urllib
import threading
import time
import urllib.request

def io_bound(url):
    
    urllib.request.urlopen(url).read()
    
URLs = ["https://python.org"] * 4

start = time.time()
    
for url in URLs:
    
    io_bound(url)
    print(f"I/O sequenziale: {time.time() - start:.2f}s")  # ~4s
    
    
print("////////////////////////////////////////////////////")
threads = [threading.Thread(target=io_bound, args=(url,)) for url in URLs]
for t in threads:
    t.start()
    
for t in threads:
    t.join()
    
print(f"I/O con 4 thread: {time.time() - start:.2f}s")  # ~1s