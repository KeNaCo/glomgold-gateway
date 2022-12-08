from abc import ABC, abstractmethod

from acquiring.domain.payment import Payment


class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, payment: Payment):
        raise NotImplementedError()
