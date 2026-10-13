from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NotificationBase(BaseModel):
    user_id: int
    title: str
    message: str
    type: str  # alert, reminder, update

class NotificationCreate(NotificationBase):
    pass

class NotificationResponse(NotificationBase):
    id: int
    is_read: bool
    created_at: datetime

    class Config:
        orm_mode = True

class NotificationUpdate(BaseModel):
    is_read: Optional[bool] = None
    title: Optional[str] = None
    message: Optional[str] = None
    type: Optional[str] = None 