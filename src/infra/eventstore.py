from src.domain.model import Event


class EventStore:
    def put(self, event: Event):
        ...

    def put_all(self, events: list[Event]):
        ...

    def get(self, entity_id: str) -> list[Event]:
        ...
