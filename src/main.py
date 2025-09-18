from .db_conf import Base, engine
from fastapi import FastAPI
from apiSCA import app

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5678)