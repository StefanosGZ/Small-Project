from datetime import datetime
#FastApi could also be used as well
from flask import Flask, request, jsonify

# If you want to test the code using Curl, the link when running the code is
# http://127.0.0.1:5000
class Order:
    def __init__(self, cart_value, delivery_distance, number_of_items, time):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time = time
        self.delivery_fee = 0

    def check_if_under_10(self):
        if self.cart_value < 1000:
            self.delivery_fee += 1000-self.cart_value

    def check_distance(self):
        self.delivery_fee += 200
        self.delivery_distance -= 1000
        while self.delivery_distance > 0:
            self.delivery_fee += 100
            self.delivery_distance -= 500

    def check_item_count(self):
        if self.number_of_items > 12:
            self.delivery_fee += 120
        if self.number_of_items > 4:
            self.delivery_fee += (self.number_of_items-4)*50

    def check_time(self):
        time = datetime.strptime(self.time, "%Y-%m-%dT%H:%M:%SZ")
        date = time.date()

        if date.weekday() == 4 and 15 <= time.hour <= 19:
            # The if below is sort of pointless but as it was 15-19,
            # but I could not figure out if it means literally between 15.00-19.00
            # So the if is to check the 19.00 part. Otherwise I would've just put time.hour<19
            if time.hour == 19 and time.minute > 0:
                pass
            else:
                self.delivery_fee *= 1.2

app = Flask(__name__)

# Takes only Post requests to the root route
@app.route('/', methods=['POST'])
def main():
    Tilaus = Order(request.json['cart_value'], request.json['delivery_distance'], request.json['number_of_items'], request.json['time'])
    if Tilaus.cart_value >= 10000:
        pass
    else:
        Tilaus.check_if_under_10()
        Tilaus.check_distance()
        Tilaus.check_item_count()
        Tilaus.check_time()
        if Tilaus.delivery_fee >= 1500:
            Tilaus.delivery_fee = 1500
    # The object Tilaus could be saved into a dictionary if we wanted to get back to it after a new order is set
    # This returns only the wanted JSON. It does not showcase it in the link => Use Postman,Curl, etc.
    return jsonify(delivery_fee=Tilaus.delivery_fee)

if __name__ == '__main__':
    app.run(debug=True)
