class UnitOfWork:
    """
    with UnitOfWork(engine) as uow:
        repo = UserRepository(uow.engine)
        user_repository.create(new_user)
        retrieved_user = user_repository.find_by_id(new_user.id)
        retrieved_user.name = "Updated John"
        user_repository.update(retrieved_user)
    """

    def __init__(self, engine):
        self.engine = engine

    def __enter__(self):
        self.transaction = self.engine.begin().__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.transaction.commit()
        else:
            self.transaction.rollback()
        self.transaction.close()
