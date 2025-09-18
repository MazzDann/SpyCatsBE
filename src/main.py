from .db_conf import Base, engine

Base.metadata.create_all(bind=engine)