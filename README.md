# Wolt API
**Stefanos Zafiris**
  
This is a small project assignment given by Wolt for their summer internships. The code is made in Python 
using the flask library to build the API. I have also done some unittesting
(all the keypoints in the github) that you can try. As it was not required I did not make
any frontend stuff, so to test the code use Postman or Curl or other similar software 
to try if the code works. As it was not requested, the code does not check if the 
given values are in a correct way. So it automatically assumes that they're right, and will break if they are not.


## Starting the code
- Open the API.py file in IDE of your choosing (PyCharm, etc...)
- Install the flask  library by putting the following line into your console:   
 **$ pip install -U Flask**  

- Run the API.py files code.  

- Copy the link in your console  
**http://127.0.0.1:5000**

- Try the code by using a POST method with some kind of JSON that is in the same format as this:  
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}

 - One way is to curl it:  
 **curl -X POST http://127.0.0.1:5000
   -H 'Content-Type: application/json'
   -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}'**

- Second is using Postman with a POST to http://127.0.0.1:5000 and select body -> raw, press the text dropdown menu and select 
JSON then paste the wanted JSON in the right format   
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}  
and send.

###Unittest
I made some basic unittests in the TestAPI.py file.
You can just run the file and it will test everything. All the tests were made similiar to the
examples in the github file.
