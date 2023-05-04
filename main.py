from fastapi import FastAPI
import uvicorn
import jwt 
from app.db.database import Base,engine
from app.routers import user

def create_tables():
  Base.metadata.create_all(bind=engine)
create_tables()




app = FastAPI()
app.include_router(user.router)


            
    

if __name__ == '__main__':
  uvicorn.run(app, port=8000, host='127.0.0.1')
          