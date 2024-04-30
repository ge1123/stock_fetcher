from fastapi import FastAPI
from routers.item_router import router as item_router

app = FastAPI()
app.include_router(item_router)
