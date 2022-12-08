from acquiring.domain import Payment, Processor


def test_process_one_payment_should_success():
    """
    This feels wrong. Processors are not processing payments, they are authorizing, capturing, debiting etc.
    How payments are processed depends on processor and payment in question. So our only way to control is to pick
    this combination and hide how it's done for input. So processors are in general processing payments.
    """
    payment = Payment()
    processor = Processor()

    assert not payment.is_processed()
    processor.process(payment)
    assert payment.is_processed()
