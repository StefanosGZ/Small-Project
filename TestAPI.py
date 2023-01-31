from flask import Flask
from API import Order,main
import unittest
app = Flask(__name__)

# These tests test the examples in the github page of the assignment
class Testcalc(unittest.TestCase):

    def setUp(self):
        self.order1 = Order(790, 2235, 4, "2021-10-12T13:00:00Z")
        self.order2 = Order(1000, 1499, 5, "2021-10-15T19:00:00Z")
        self.order3 = Order(1000, 1500, 10, "2021-10-15T19:01:00Z")
        self.client = app.test_client()

    # Tests the check_if_under_10
    def test_under10(self):
        self.order1.check_if_under_10()
        self.order2.check_if_under_10()
        self.order3.check_if_under_10()

        self.assertEqual(self.order1.delivery_fee, 210)
        self.assertEqual(self.order2.delivery_fee, 0)
        self.assertEqual(self.order3.delivery_fee, 0)

    # Tests the check_distance function
    def test_distance(self):
        self.order1.check_distance()
        self.order2.check_distance()
        self.order3.check_distance()

        self.assertEqual(self.order1.delivery_fee, 500)
        self.assertEqual(self.order2.delivery_fee, 300)
        self.assertEqual(self.order3.delivery_fee, 300)

        self.order3.delivery_distance = 1501
        self.order3.delivery_fee = 0
        self.order3.check_distance()

        self.assertEqual(self.order3.delivery_fee, 400)

    # Tests the check_item_count function
    def test_item_count(self):
        self.order1.check_item_count()
        self.order2.check_item_count()
        self.order3.check_item_count()

        self.assertEqual(self.order1.delivery_fee, 0)
        self.assertEqual(self.order2.delivery_fee, 50)
        self.assertEqual(self.order3.delivery_fee, 300)

        self.order3.number_of_items = 13
        self.order3.delivery_fee = 0
        self.order3.check_item_count()

        self.assertEqual(self.order3.delivery_fee, 570)

    # Tests the check_time function
    def test_time(self):
        self.order1.delivery_fee = 10
        self.order2.delivery_fee = 10
        self.order3.delivery_fee = 10

        self.order1.check_time()
        self.order2.check_time()
        self.order3.check_time()

        self.assertEqual(self.order1.delivery_fee, 10)
        self.assertEqual(self.order2.delivery_fee, 10*1.2)
        self.assertEqual(self.order3.delivery_fee, 10)


    # Tests if the cart value>=100€ returns delivery fee = 0 in the main()
    @app.route('/test_cartvalue')
    def test_cartvalue(self):
        # Over or as much as 100€
        data = {"cart_value": 10000, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
        with app.test_request_context(json=data):
            result = main()
            self.assertEqual(result.get_json(), {"delivery_fee": 0})

        #Under 100€
        data2 = {"cart_value": 9999, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
        with app.test_request_context(json=data2):
            result2 = main()
            self.assertNotEqual(result2.get_json(), {"delivery_fee": 0})

    # Tests if the delivery fee >= 15€ -> delivery fee = 15€ command works
    @app.route('/test_delivery_fee_over15')
    def test_delivery_fee_over15(self):
        # Delivery fee under 15€
        data = {"cart_value": 710, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
        with app.test_request_context(json=data):
            result = main()
            self.assertNotEqual(result.get_json(), {"delivery_fee": 1500})

        # Delivery fee over 15€
        data2 = {"cart_value": 100, "delivery_distance": 5000, "number_of_items": 15, "time": "2021-10-15T16:00:00Z"}
        with app.test_request_context(json=data2):
            result2 = main()
            self.assertEqual(result2.get_json(), {"delivery_fee": 1500})



if __name__=='__main__':
    unittest.main()