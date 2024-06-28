from .models import Order, OrderItem, Cancellation, Return, Refund

def create_order(user, items):
    order = Order.objects.create(user=user, status='placed')
    for item in items:
        OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'])
    return order

def cancel_order(order_id, reason):
    order = Order.objects.get(id=order_id)
    order.status = 'cancelled'
    order.save()
    Cancellation.objects.create(order=order, reason=reason)

def return_order(order_id, reason):
    order = Order.objects.get(id=order_id)
    Return.objects.create(order=order, reason=reason)

def process_refund(order_id, amount):
    order = Order.objects.get(id=order_id)
    Refund.objects.create(order=order, amount=amount)