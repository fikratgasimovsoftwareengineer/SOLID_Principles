from domain.models.payment import Payment

class InvoiceGenerator:
    """Responsabilità: SOLO genera PDF fattura"""
    
    def generate(self, payment: Payment) -> str:
        filename = f"invoice_{payment.id}.pdf"
        print(f"[PDF] Fattura generata: {filename}")
        return filename 