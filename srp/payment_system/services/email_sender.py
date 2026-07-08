from domain.models.payment import Payment

class ReceiptEmailSender:
    """Responsabilità: SOLO invia email"""
    
    def send(self, email: str, payment: Payment) -> None:
        print(f"[EMAIL] Ricevuta inviata a {email}")
        print(f"[EMAIL] Importo: {payment.amount}€")