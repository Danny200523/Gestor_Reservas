# app/db/db.py
import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

# 1) Cargar .env
load_dotenv()

# 2) Leer variables EXACTAMENTE como las tienes en tu .env
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host", "127.0.0.1")
PORT = os.getenv("port")            # <- string; puede ser None
DBNAME = os.getenv("dbName")

# 3) Validar obligatorios
missing = [k for k,v in {
    "user": USER, "password": PASSWORD, "dbName": DBNAME
}.items() if not v]
if missing:
    raise RuntimeError(f"Faltan variables en .env: {', '.join(missing)}")

# 4) Elegir driver que tengas instalado (recomiendo pymysql)
#    pip install pymysql
DRIVER = "mysql+pymysql"

# 5) Construir URL (si no hay PORT, no lo incluyas)
if PORT and PORT.strip():
    DATABASE_URL = f"{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
else:
    DATABASE_URL = f"{DRIVER}://{USER}:{PASSWORD}@{HOST}/{DBNAME}"

# 6) TiDB Cloud requiere SSL
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"ssl": {"ssl": True}}
)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
