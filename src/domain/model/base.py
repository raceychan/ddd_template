import typing as ty
from dataclasses import dataclass

frozen = dataclass(frozen=True, slots=True, kw_only=True)


@ty.dataclass_transform(frozen_default=True, kw_only_default=True)
class Frozen:
    ...


class Model:
    ...


@frozen
class Message(Frozen):
    message_id: str
    entity_id: str


@frozen
class Event(Message):
    ...


@frozen
class Command(Message):
    ...


@frozen
class Query(Message):
    ...


class Entity(Model):
    entity_id: str
