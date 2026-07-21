import asyncio
import time
import threading ### solo per printare il nome del thread, non è necessario per il funzionamento
from concurrent.futures import ThreadPoolExecutor

def task_pesante_bedrock(id_richiesta):
    thread_name = threading.current_thread().name
    
    print("===========***************START**************================================")
    print(f"Task richiesta per {id_richiesta} iniziato in {thread_name} (attesa 2 secondi)...")

  
    print(f"Task richiesta per {id_richiesta} completato in {thread_name}!")
    print("===========++++++++++++COMPLETATA+++++++++================================")
    
NUM_WORKERS = 5

async def main():
    
    print(f"--- INIZIO SIMULAZIONE (Workers: {NUM_WORKERS}) ---")
    
    executor = ThreadPoolExecutor(max_workers=NUM_WORKERS)
    
    loop = asyncio.get_event_loop()
    loop.set_default_executor(executor)
    
    
    start_time = time.time()
    tasks = []
    
    
    for i in range(10):
        task = asyncio.to_thread(task_pesante_bedrock, i)
        tasks.append(task)


    results = await asyncio.gather(*tasks)
    
    end = time.time()
    total_time = end - start_time
    
    print(f"\n--- REPORT FINALE ---")
    print(f"Totale Richieste: 10")
    print(f"Tempo stimato sequenziale (senza thread): {10 * 2} secondi")
    print(f"Tempo REALE impiegato: {total_time:.2f} secondi")
    
    
    if total_time < 3:
        print("Ottimo! La concorrenza ha funzionato bene.")
    elif total_time < 10:
        print("Buono, ma c'è margine di miglioramento.")
    else:
        print("Attenzione: sembra che i thread non stiano funzionando come previsto.")
        
        
if __name__ == "__main__":
    asyncio.run(main())