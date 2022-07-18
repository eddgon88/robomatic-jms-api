from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from ..services.jmsService import Sender

class JmsParams(BaseModel):
    engine: str
    host: str
    port: str
    queueName: str    
    user: Optional[str] = None
    password: Optional[str] = None    
    message: Optional[str] = None

router = APIRouter(prefix="/jms-api/v1")

@router.post("/sendqueue", status_code=200)
def consume(params: JmsParams):
    print("sending: " + params.host)
    print(str(params))
    return Sender.sendqueue(params.dict())