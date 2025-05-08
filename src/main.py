from fastapi import FastAPI
import sys
import os
import uvicorn

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.api.main_router import main_router


app = FastAPI()
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
