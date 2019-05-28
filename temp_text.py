import Adafruit_DHT
from twilio.rest import Client
import time
from variables import *
import schedule

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio=17
temperature = 0
humidity = 0
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
 
# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.

# if humidity is not None and temperature is not None:
#   print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
# else:
#   print('Failed to get reading. Try again!')


destination_phone_number = str(input("Phone number to send results to?"))
client = Client(account_sid, auth_token)
# message = client.messages \
#     .create(
#         body="The temperature today is ",
#         from_=twilio_phone_number,
#         to=destination_phone_number
#     )

def send_text():
    client.messages.create(body="The temperature today is " + temperature,to=destination_phone_number,from_=twilio_phone_number)

schedule.every().day.at("7:00").do(get_temp)
schedule.every().day.at("7:00").do(send_text)
