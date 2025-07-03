from pydantic import BaseModel
from datetime import date
from enum import Enum

class SubscriptionType(str, Enum):
    NORMAL = "NORMAL"
    PRIME = "PRIME"
    VIP = "VIP"

class DeliveryOrderDTO(BaseModel):
    date: date
    vendor_name: str
    total_orders: int
    subscription: SubscriptionType

class VendorDTO(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True