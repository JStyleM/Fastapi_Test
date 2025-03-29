from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mssql+pyodbc://@localhost/FastAPI?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

engine = create_engine(DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
