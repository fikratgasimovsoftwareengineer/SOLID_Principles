from domain.models.payment import Payment

class PaymentProcessor:
    """Responsabilità: SOLO elabora il pagamento"""
    
    def process(self, amount: float) -> Payment:
        print(f"[PAYMENT] Elaboro pagamento {amount}€")
        return Payment(
            id     = "pay-001",
            amount = amount,
            status = "success"
        )