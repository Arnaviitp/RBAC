from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class SubscriptionType(enum.Enum):
    NORMAL = "NORMAL"
    PRIME = "PRIME"
    VIP = "VIP"

class Vendor(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)

class DeliveryOrder(Base):
    __tablename__ = 'delivery_orders'
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer)
    date = Column(Date)
    total_orders = Column(Integer)
    vendor_name = Column(String)
    subscription = Column(Enum(SubscriptionType))