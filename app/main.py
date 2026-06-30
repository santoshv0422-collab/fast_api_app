from fastapi import FastAPI
from routers.company import router as company_router
from routers.job import router as job_router
from models import job as job_model, company as company_model
from database import Base, engine, SessionLocal

app = FastAPI()
print("engine is", job_model.engine)

app.include_router(company_router)
app.include_router(job_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"About": "This is a FastAPI application."}

@app.get("/contact")
def read_contact():
    return {"Contact": "santoshv0422@gmail.com"} 