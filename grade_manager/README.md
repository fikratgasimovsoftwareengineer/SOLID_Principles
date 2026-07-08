grade_manager/
│
├── main.py
│
├── domain/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   └── interfaces/
│       ├── __init__.py
│       ├── i_repository.py      ← inserimento + cancellazione + ricerca
│       ├── i_calculator.py      ← calcoli sui voti
│       └── i_reporter.py        ← generazione report
│
├── services/
│   ├── __init__.py
│   ├── student_repository.py    ← implementa i_repository
│   ├── grade_calculator.py      ← implementa i_calculator
│   └── grade_reporter.py        ← implementa i_reporter
│
└── app/
    ├── __init__.py
    └── grade_manager.py         ← orchestratore