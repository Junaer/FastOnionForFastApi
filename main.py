import os
import sys


class FastApiOnion:
    def __init__(self, path=''):
        self.path = path
        self.db = 'db'
        self.migrations = 'migrations'
        self.models = 'models'
        self.repositories = 'repositories'
        self.routers = 'routers'
        self.schemas = 'schemas'
        self.service = 'service'
        self.utils = 'utils'

    def create_structure(self):
        os.mkdir(f'{self.path}')
        os.mkdir(f'{self.path}/{self.db}')
        db = open(f'{self.path}/{self.db}/db.py', 'w')
        db.write(db_code)
        db.close()
        config = open(f'{self.path}/{self.db}/config.py', 'w')
        config.write(config_code)
        config.close()
        os.mkdir(f'{self.path}/{self.migrations}')
        os.mkdir(f'{self.path}/{self.models}')
        os.mkdir(f'{self.path}/{self.repositories}')
        os.mkdir(f'{self.path}/{self.routers}')
        os.mkdir(f'{self.path}/{self.schemas}')
        os.mkdir(f'{self.path}/{self.service}')
        os.mkdir(f'{self.path}/{self.utils}')

    def create_app(self, name):
        open(f'{self.path}/{self.models}/{name}_models.py', 'x')
        open(f'{self.path}/{self.repositories}/{name}_repositories.py', 'x')
        open(f'{self.path}/{self.routers}/{name}_routers.py', 'x')
        open(f'{self.path}/{self.schemas}/{name}_schemas.py', 'x')
        open(f'{self.path}/{self.service}/{name}_service.py', 'x')
        
if __name__ == "__main__":
    if sys.argv[1] == 'create':
        create = FastApiOnion(sys.argv[2])
        create.create_structure()
    if sys.argv[1] == 'app':
        app = FastApiOnion(sys.argv[2])
    if sys.argv[1] == '--info':
        print("""Script commands:
_________________________________________
|    create 'project_name'               |
|    app 'project_name' 'app_name'       |
|________________________________________|
        """)


db_code = """import asyncio
from typing import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from db.config import data_base


class Base(DeclarativeBase):
    pass


engine = create_async_engine(url=data_base,
                             echo=False)

async_session_factory = async_sessionmaker(engine)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session

"""

config_code = """from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv('TOKEN')

data_base = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

"""
