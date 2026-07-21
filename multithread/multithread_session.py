import asyncio
import threading
import os
import time
from concurrent.futures import ThreadPoolExecutor


def servizio_di_lento(utente_id:int)->str:
    
    nome_thread = threading.current_thread().name
    print(f"Thread {nome_thread} sta servendo l'utente {utente_id}\n")
    
    time.sleep(2)
    print("*************************************************************\n")
    print(f"{nome_thread} ha finito di servire l'utente {utente_id}\n")
    print("*************************************************************\n")
    
    return f"Risultati_Utente_{utente_id}"

async def main():
    
    
    core_cpu = os.cpu_count() or 2
    
    # per i operazione i/o bound, si moltiplicano i core.
    
    max_workers = core_cpu * 2
    
    print(f"Hardware : Rilevati {core_cpu} core della CPU")
    print(f"Configurato il threadpoolexecutor con {max_workers} thread (workers)\n")


    loop = asyncio.get_running_loop()
    
    richiest_utenti  = range(1, 11)
    
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 4. Creazione dei Task
        # Deleghiamo ogni chiamata 'servizio_lento' al nostro executor.
        # run_in_exec   utor è un metodo che permette di eseguire una funzione bloccante in un thread separato, senza bloccare l'event loop principale.
        tasks = [
            loop.run_in_executor(executor, servizio_di_lento, utente_id)
            for utente_id  in richiest_utenti
        ]
        
        print("Tutti i task sono stati delegati al ThreadPoolExecutor. Attendo i risultati...\n")
        risultati = await asyncio.gather(*tasks)
        
    tempo_totale = time.time() - start_time
    
    print(f"\nTutti i risultati sono stati raccolti: {risultati}")
    print(f"Tempo totale impiegato {tempo_totale: .2f} secondi per lungo di richieste di {len(richiest_utenti)} utenti")    
    
    
if __name__ == "__main__":
    asyncio.run(main())