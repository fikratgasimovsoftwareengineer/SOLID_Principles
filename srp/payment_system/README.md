```sh
payment_system/
│
├── main.py
│
├── domain/
│   ├── __init__.py
│   └── models/
│       ├── __init__.py
│       └── payment.py
│
├── services/
│   ├── __init__.py
│   ├── payment_processor.py
│   ├── payment_repository.py
│   ├── receipt_email_sender.py
│   ├── invoice_generator.py
│   └── payment_service.py
│
└── tests/
    ├── __init__.py
    └── test_payment_service.py
```