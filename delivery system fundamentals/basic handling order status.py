class Order:    
    def __init__(self,order_id,customer_id,status):
        self.order_id = order_id
        self.customer_id = customer_id
        self.status = status
    def marked_delivered(self):
        self.status = "delivered"
order1 = Order(1,1,"pending")
print(order1.status)
order1.marked_delivered()
print(order1.status)