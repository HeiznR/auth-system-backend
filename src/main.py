from fastapi import FastAPI
import uvicorn
from src.api.main_router import main_router


app = FastAPI()
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
