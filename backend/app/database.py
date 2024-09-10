from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from backend.app.config import settings

async_engine = create_async_engine(settings.database_url, echo=True)

async_session = async_sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)
