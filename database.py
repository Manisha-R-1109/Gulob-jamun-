from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:password@localhost/gulobjamundb"

engine = create_engine(DATABASE_URL)

print("Database Connected")
