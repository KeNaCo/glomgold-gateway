from acquiring.domain import Payment, PaymentProcessor
from acquiring.domain.stub_processor.stub_processor import StubPayment, StubProcessor

from . import helpers


def test_process_one_payment_should_be_processed():
    """
    This feels wrong. Processors are not processing payments, they are authorizing, capturing, debiting etc.
    How payments are processed depends on processor and payment in question. So our only way to control is to pick
    this combination and hide how it's done for input. So processors are in general processing payments.
    """
    payment: Payment = StubPayment()
    processor: PaymentProcessor = StubProcessor()

    assert not payment.is_processed
    processor.process(payment)
    helpers.assert_PaymentIsProcessed(processor, payment)
