from sqlmodel import Session, create_engine
from app.core.config import settings

# Para Postgres (psycopg3), não há connect_args especiais
engine = create_engine(
    settings.database_url,
    echo=False,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
)


def get_session():
    with Session(engine) as session:
        yield session
