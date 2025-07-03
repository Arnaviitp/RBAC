def parse_delivery_file(file_content: str):
    orders = []
    lines = file_content.strip().split('\n')
    for line in lines:
        vendor_name, date, total_orders, subscription = line.split(',')
        orders.append({
            'vendor_name': vendor_name,
            'date': date,
            'total_orders': int(total_orders),
            'subscription': subscription
        })
    return orders