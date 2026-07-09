# Grade Manager

## Descrizione del progetto
Questo repository contiene un semplice sistema di gestione degli studenti e delle loro valutazioni basato su principi SOLID, in particolare SRP (Single Responsibility Principle) e ISP (Interface Segregation Principle).

Il progetto è organizzato in tre parti principali:
- `domain`: modelli e interfacce astratte che definiscono il dominio dell'applicazione
- `services`: implementazioni concrete dei repository e dei calcolatori di voti
- `app`: orchestratore che coordina repository e calcolatore per realizzare le operazioni sull'applicazione

## Struttura dei file

- `main.py`
  - punto di ingresso dell'applicazione
  - crea l'istanza di `GradeManager` con `InMemoryStudentRepository` e `GradeCalculator`
  - aggiunge studenti, crea assignment e mostra i risultati

- `app/grade_manager.py`
  - classe `GradeManager` che funge da orchestratore
  - riceve due dipendenze tramite iniezione: `IStudentRepository` e `IGradeCalculator`
  - coordina operazioni come aggiunta/rimozione studenti e gestione assignment

- `domain/interfaces/i_student_repository.py`
  - interfaccia `IStudentRepository`
  - definisce le operazioni di base sul repository studenti
    - `_create_student`
    - `_delete_student`
    - `_find_by_id`
    - `_find_all`

- `domain/interfaces/i_grade_calculator.py`
  - interfaccia `IGradeCalculator`
  - definisce le operazioni legate ai voti e ai calcoli
    - `insert_student_assignments`
    - `get_average`
    - `assign_score`

- `domain/models/students.py`
  - modello `Student` con `pydantic`
  - attributi: `id`, `matricola_num`, `dipartimento`, `campo_del_studio`

- `domain/models/assignment.py`
  - modello `Assignment` con `pydantic`
  - attributi: `student_id`, `materia`, `voti`

- `domain/models/logger.py`
  - wrapper semplice su `logging`
  - classe `Logger` usata da `GradeManager`, `InMemoryStudentRepository` e `GradeCalculator`

- `services/student_repository.py`
  - classe `InMemoryStudentRepository`
  - implementa `IStudentRepository`
  - salva gli studenti in memoria usando un dizionario e un set per l'unicità

- `services/grade_calculator.py`
  - classe `GradeCalculator`
  - implementa `IGradeCalculator`
  - memorizza gli assignment in memoria e calcola medie e valutazioni

## Flusso di integrazione e funzionamento

1. `main.py` crea l'istanza di `GradeManager` passando `InMemoryStudentRepository` e `GradeCalculator`.
2. `GradeManager.add_student(...)` costruisce un oggetto `Student` e chiama `_create_student` sul repository.
3. `GradeManager.create_assigment(...)` costruisce un oggetto `Assignment` e lo passa a `GradeCalculator.insert_student_assignments(...)`.
4. `GradeCalculator` mantiene in memoria gli assignment per studente e restituisce la lista aggiornata di assignment.
5. `GradeManager.remove_student(...)` verifica l'esistenza dello studente tramite `_find_by_id` e poi chiama `_delete_student` sul repository.
6. `GradeManager.calculate_avverage_score(...)` recupera lo studente dal repository e usa `GradeCalculator.get_average(...)` per calcolare la media dei voti.
7. `GradeManager.insert_grade_per_studente(...)` usa `GradeCalculator.assign_score(...)` per trasformare un punteggio numerico in una lettera di valutazione.

## Dettagli delle classi

### `GradeManager`
- ruoli:
  - orchestrare l'interazione tra repository e calcolatore
  - mantenere separate le responsabilità
- dipendenze:
  - `IStudentRepository` per operazioni CRUD sugli studenti
  - `IGradeCalculator` per gestione assignment e calcolo voti

### `InMemoryStudentRepository`
- salva gli studenti in memoria
- garantisce che ogni `student.id` sia univoco
- fornisce metodi per:
  - creare uno studente
  - cancellare uno studente
  - cercare uno studente per ID
  - ottenere tutti gli studenti

### `GradeCalculator`
- mantiene un archivio in memoria degli assignment per studente
- registra l'aggiunta delle materie e dei voti
- calcola la media aritmetica dei voti per studente
- traduce punteggi numerici in voti letterali (`A`, `B`, `C`, `D`, `E`)

### Modelli
- `Student`
  - rappresenta i dati principali di uno studente
- `Assignment`
  - rappresenta i voti di una materia assegnata a uno studente
- `Logger`
  - fornisce logging centralizzato per tracciare operazioni e avvisi

## Come eseguire

Eseguire `main.py` per vedere un esempio d'uso:

```bash
python main.py
```

## Note architetturali

- Le interfacce `IStudentRepository` e `IGradeCalculator` rispettano ISP: ogni classe implementa solo i metodi necessari.
- `GradeManager` segue SRP: si occupa esclusivamente di orchestrare le operazioni e non implementa la logica di storage o calcolo.
- L'uso di modelli `pydantic` semplifica la validazione dei dati per `Student` e `Assignment`.

## Estensioni possibili

- aggiungere un repository basato su database reale
- aggiungere reportistica con una classe `GradeReporter`
- estendere `GradeCalculator` con calcoli avanzati
- aggiungere gestione delle eccezioni e validazione input più robusta
