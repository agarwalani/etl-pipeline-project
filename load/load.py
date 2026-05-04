from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def load_data(df):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db = os.getenv("DB_NAME")

    engine = create_engine(f"postgresql://{user}:{password}@localhost:5432/{db}")
    
    df.to_sql('users', engine, if_exists='append', index=False)