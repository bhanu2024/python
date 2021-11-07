class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    # def check_lowest_price(self, lowest_price):
    #     price = self.price
    #     return price

# ------------------------------My code-------------------------#

# _-------------------OUTPUT---------------------------#
# Paris: £13
# Berlin: £13
# Tokyo: £255
# Sydney: £349
# Istanbul: £48
# Kuala Lumpur: £257
# New York: £155
# San Francisco: £179
# Cape Town: £305


# import requests
# import datetime
# from pprint import pprint
#
# TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
# TEQUILA_API_KEY = "5k_VwHf0AXda_aMqjh1PU6WSYQ9i7XU_"
#
# class FlightData:
# # This class is responsible for structuring the flight data.
#
#     def get_price(self, code, city_name):
#         tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
#         date_to = datetime.datetime.now() + datetime.timedelta(days=180)
#         headers = {
#                     "apikey": TEQUILA_API_KEY
#                 }
#
#         search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
#         query_search = {
#             "fly_from": "LON",
#             "fly_to": code,
#             "date_from": tomorrow.strftime("%d/%m/%Y"),
#             "date_to": date_to.strftime("%d/%m/%Y")
#         }
#         searching = requests.get(url=search_endpoint, headers=headers, params=query_search)
#         search_result = searching.json()["data"]
#         price = search_result[0]["price"]
#         gbp = round(price * 0.86)
#
#         print(f"{city_name}: £{gbp}")