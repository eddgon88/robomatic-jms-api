# application/__init__.py
from fastapi import FastAPI
from .routers import jmsRouter

#app = FastAPI()
#app.include_router(jmsRouter.router)

def create_app():
    app = FastAPI()
    app.include_router(jmsRouter.router)
    return app
        
