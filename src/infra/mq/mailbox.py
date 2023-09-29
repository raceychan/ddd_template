import abc
import typing as ty

from src.domain.model import Message


class Broker(abc.ABC):
    def put(self, message: Message) -> None:
        ...

    def get(self) -> Message:
        ...

    @abc.abstractproperty
    def size(self) -> int:
        "Return current message size"
        ...

    def volume(self) -> int:
        ...


class Mailbox:
    broker: Broker

    def get(self) -> Message:
        ...

    def put(self, message: Message):
        ...
