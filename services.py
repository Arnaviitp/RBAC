from models import DeliveryOrder, Vendor
from sqlalchemy.orm import Session
from schemas import DeliveryOrderDTO

def save_orders(db: Session, orders_data):
    for order in orders_data:
        db_order = DeliveryOrder(
            vendor_name=order['vendor_name'],
            date=order['date'],
            total_orders=order['total_orders'],
            subscription=order['subscription']
        )
        db.add(db_order)
    db.commit()

def get_orders(db: Session, vendor_name: str, date=None):
    query = db.query(DeliveryOrder).filter(DeliveryOrder.vendor_name == vendor_name)
    if date:
        query = query.filter(DeliveryOrder.date == date)
    return query.all()