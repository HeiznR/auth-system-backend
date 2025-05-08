from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from db.database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def create():
        raise NotImplementedError

    @abstractmethod
    async def read():
        raise NotImplementedError

    @abstractmethod
    async def update():
        raise NotImplementedError

    @abstractmethod
    async def delete_one():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def create(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            session.commit()
            return res.scalar_one()

    async def read(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            return res

    async def update():
        raise NotImplementedError

    async def delete_one():
        raise NotImplementedError
