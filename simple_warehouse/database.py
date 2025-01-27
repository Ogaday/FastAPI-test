from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# user=os.environ['POSTGRES_USER']
# password=os.environ["POSTGRES_PASSWORD"]
# postgresserver=os.environ["POSTGRES_SERVER"]
# db=os.environ["POSTGRES_DB"]

# engine= f"postgresql://{user}:{password}@{server}/{db}"

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
