import asyncio
import random
import time
from datetime import datetime


# Definiamo dei colori ANSI per il terminale per distinguere visivamente i task
COLORS = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m']
RESET = '\033[0m'

def task_bloccante(task_id, passi):
    """
    Questa funzione simula un lavoro pesante/bloccante (usando time.sleep).
    Verrà eseguita all'interno di un Thread separato.
    """
    # Impostiamo colore e spazio per creare colonne visive nel terminale
    colore = COLORS[task_id - 1]
    spazio = " " * ((task_id - 1) * 20) 
    
    print(f"{spazio}{colore}[Task {task_id}] INIZIATO{RESET}")
    
    for step in range(1, passi + 1):
        # Simuliamo un lavoro che richiede un tempo variabile tra 0.2 e 0.8 secondi
        attesa = random.uniform(0.2, 0.8)
        time.sleep(attesa)
        
        # Catturiamo il millisecondo esatto per farti vedere la sequenza temporale
        ora_attuale = datetime.now().strftime('%S.%f')[:-3]
        print(f"{spazio}{colore}Task {task_id}: step {step}/{passi} ({ora_attuale}s){RESET}")
        
    print(f"{spazio}{colore}[Task {task_id}] FINITO{RESET}")
    return f"Risultato elaborazione {task_id}"

async def main():
    print("Inizio esecuzione parallela dei 5 task...\n")
    print("Task 1              Task 2              Task 3              Task 4              Task 5")
    print("-" * 100)
    
    tasks = []
    for i in range(1, 6):
        
        passi_causali = random.randint(3,6)
        task_courotune = asyncio.to_thread(task_bloccante, i, passi_causali)
        tasks.append(task_courotune)
        
    
    risultati = await asyncio.gather(*tasks)
    print("\n" + "-" * 100)
    print("Tutti i task sono terminati con successo!")
    print("Raccolta risultati:", risultati)
    
if __name__ == "__main__":
    asyncio.run(main())
    