from concurrent.futures import ThreadPoolExecutor
import requests
import time
#################################################################################################################################
#--------------------THREAD POOLING CON IL 10 WORKER & THREAD CHE ESEGUONO IL CODICE BYTECODE IN THE STESSO TEMPO --------------#
#################################################################################################################################


urls = ["https://www.uninettunouniversity.net/it/default.aspx"] * 10

def scarica_url(url):
    return requests.get(url, timeout=10).status_code

def scarica_threadpool(urls, max_workers=5):
    
    with ThreadPoolExecutor (max_workers=max_workers) as pool:
        risultati = list(pool.map(scarica_url, urls))
    return risultati


inizio = time.time()
scarica_threadpool(urls)
print(f"Tempo ThreadPool: {time.time() - inizio:.2f}s")
# Output: ~2 secondi (10 URL / 5 thread = 2 batch)