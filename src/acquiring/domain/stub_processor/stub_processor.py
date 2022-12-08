from acquiring.domain import Payment, Processor


class StubPayment(Payment):
    def __init__(self):
        self._processed = False

    @property
    def is_processed(self):
        return self._processed

    def set_processed(self):
        self._processed = True


class StubProcessor(Processor):
    def process(self, payment: Payment):
        if isinstance(payment, StubPayment):
            payment.set_processed()
