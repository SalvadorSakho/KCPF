from sqlalchemy import QueuePool

from configs.ch_config import ch_url
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

engine = create_async_engine(url=ch_url, poolclass=QueuePool, pool_size=3, max_overflow=2)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_cursor() -> AsyncSession:
    async with async_session() as ch_session:
        yield ch_session
