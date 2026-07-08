from domain.models.payment import Payment
from services.payment_processor import PaymentProcessor
from services.payment_repository import PaymentRepository
from services.email_sender import ReceiptEmailSender
from services.invoice_generator import InvoiceGenerator

class PaymentService:
    
    def __init__(self):
        self._processor = PaymentProcessor()
        self._repository = PaymentRepository()
        self._email = ReceiptEmailSender()
        self._invoice = InvoiceGenerator()
        
        
    def complete_payment(
        self,
        amount: float,
        email: str
    ) -> Payment:
        
        print("\n" + "=" * 40)
        print("  Elaborazione pagamento")
        print("=" * 40)
        
        
        # step 1
        payment = self._processor.process(amount)
        
        # step 2
        self._repository.save(payment)
        
        #step 3
        self._email.send(email, payment)
        
        # step 4 — fattura
        self._invoice.generate(payment)
        
             
        print("=" * 40)
        print(f"  Completato! Status: {payment.status}")
        print("=" * 40)
        
        return payment
