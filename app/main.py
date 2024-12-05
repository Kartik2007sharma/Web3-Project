from fastapi import FastAPI
from database import Base, engine
from routes import tokens, swaps

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tokens.router, prefix="/api")
app.include_router(swaps.router, prefix="/api")
