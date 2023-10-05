class Order:

    def __init__(self, total_price, status, client):
        self._total_price = total_price
        self._status = status
        self._client = client

    def check_total_price(self):
        print(f"Order Price: {self._total_price}") 

    def check_status(self):
        print(f"Order Status: {self._status}")