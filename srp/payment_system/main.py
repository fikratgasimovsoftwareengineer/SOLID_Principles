from services.payment_service import PaymentService

if __name__ == "__main__":
    service = PaymentService()
    
    payment = service.complete_payment(
        amount = 99.99,
        email  = "fikrat@email.com"
    )
    
    print(f"\nPayment ID: {payment.id}")
    print(f"Amount:     {payment.amount}€")
    print(f"Status:     {payment.status}")
    print(f"Created:    {payment.created_at}")