from acquiring.domain.payment import Payment


class Processor:
    def process(self, payment: Payment):
        raise NotImplementedError()
