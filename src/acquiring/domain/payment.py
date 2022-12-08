from abc import ABC, abstractmethod


class Payment(ABC):
    @property
    @abstractmethod
    def is_processed(self):
        raise NotImplementedError()
