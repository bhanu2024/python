#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_CODE = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY_CODE, destination["iataCode"], tomorrow, six_month_from_today)
    # lowest_price = flight_search.lowest_price(ORIGIN_CITY_CODE, destination["iataCode"], tomorrow, six_month_from_today, destination["lowestPrice"])

# --------------My code--------------#
# else:
#     from flight_data import FlightData
#     flight_data = FlightData()
#     for row in sheet_data:
#         flight_data.get_price(row["iataCode"], row["city"])


#----------------------MY CODE-------------------#
# import requests
# from pprint import pprint
#
#
# sheety_endpoint_get = "https://api.sheety.co/4a83eda7a146e41dc2b8829b2500ad49/flightDeals/prices"
#
# sheet_input = {
#     "price": {
#         "iataCode": "TESTING"
#     }
#
# }
#
# for row in range(2, 11):
#     sheety_endpoint_put = f"https://api.sheety.co/4a83eda7a146e41dc2b8829b2500ad49/flightDeals/prices/{row}"
#
#     sheety_put = requests.put(url=sheety_endpoint_put, json=sheet_input)
#
#
# sheety_data = requests.get(url=sheety_endpoint_get)
# data = sheety_data.json()
# pprint(data)
