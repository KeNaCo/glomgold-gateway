def assert_PaymentIsProcessed(processor, payment):
    """Check if payment was processed by processor."""
    assert payment.is_processed
