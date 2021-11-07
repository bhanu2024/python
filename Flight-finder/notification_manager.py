from flight_search import FlightSearch

flight_search = FlightSearch()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def notify(self, price, departure_city, departure_city_code, arrival_city, arrival_city_code, out_date, return_date):
        from twilio.rest import Client

        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = "AC9a68efcbb1c66f6907f24cb461a5ba57"
        auth_token = "204540f8ef6f10e5c580359817b2718a"
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"Lowest price alert! Only £{price} to fly from {departure_city}-{departure_city_code} to"
                 f"{arrival_city}-{arrival_city_code}, from {out_date} to {return_date}",
            from_='+15625177905',
            to='+916363851340'
        )

        print(message.sid)
