import requests
from flight_data import FlightData
from notification_manager import NotificationManager

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "5k_VwHf0AXda_aMqjh1PU6WSYQ9i7XU_"


class FlightSearch:

    def get_destination_code(self, city_name):
        # print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": TEQUILA_API_KEY
        }

        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": TEQUILA_API_KEY
        }

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")

        # # flight_data.check_lowest_price(flight_data.price)
        # if flight_data.price < lowest_price:
        #     notification_manager = NotificationManager()
        #     notification_manager.notify(
        #         flight_data.price,
        #         flight_data.origin_city,
        #         flight_data.origin_airport,
        #         flight_data.destination_city,
        #         flight_data.destination_airport,
        #         flight_data.out_date,
        #         flight_data.return_date
        #     )

        return flight_data

    # def lowest_price(self, origin_city_code, destination_city_code, from_time, to_time, l_price):
    #     check = self.check_flights(origin_city_code, destination_city_code, from_time, to_time)
    #     price = check.price
    #

# -----------------------------------------------My code----------#
#         #
#         # tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
#         # date_to = datetime.datetime.now() + datetime.timedelta(days=180)
#         #
#         # search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
#         # query_search = {
#         #     "fly_from": "LON",
#         #     "fly_to": code,
#         #     "date_from": tomorrow.strftime("%d/%m/%Y"),
#         #     "date_to": date_to.strftime("%d/%m/%Y")
#         # }
#         # searching = requests.get(url=search_endpoint, headers=headers, params=query_search)
#         # search_result = searching.json()["data"]
#         # price = search_result[0]["price"]
#         # gbp = round(price * 0.86)
#         #
#         # print(f"{city_name}: £{gbp}")
#         return code


