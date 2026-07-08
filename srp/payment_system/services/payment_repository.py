from domain.models.payment import Payment

class PaymentRepository:
    """Responsabilità: SOLO salva nel database"""
    def __init__(self):
        self._storage = {}
        
    def save(self, payment:Payment):
        self._storage[payment.id] = payment
        print(f"[DB] Salvo pagamento {payment.id}")
        
    def find_by_id(self, payment_id:str)->Payment:
        return self._storage.get(payment_id)