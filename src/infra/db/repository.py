import abc
from src.domain.model import Entity


class Repository(abc.ABC):
    def add(self, entity: Entity):
        ...

    def add_all(self, entities: list[Entity]):
        ...

    def get(self, entity_id: str) -> Entity:
        raise NotImplementedError

    def get_all(self, entity_ids: set[str]) -> list[Entity]:
        raise NotImplementedError

    def update(self, entity: Entity):
        ...

    def remove(self, entity_id: str):
        ...
