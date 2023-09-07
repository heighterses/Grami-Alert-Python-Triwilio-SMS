import requests
from twilio.rest import Client

account_sid = "AC4aa66672501e297d6727cfad4b99a739"
auth_token = "221a34f12bedcf5ae87d7547e6f50e50"

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
MY_LAT = float(33.684422)
MY_LONG = float(73.047882)
city = "lahore"
api_key = "f6c37586c1df36f113bd0b8844029b93"

parameters = {
    # "lat": MY_LONG,
    # "lon": MY_LAT,
    "q": city,
    "appid": api_key,
    "cnt": 7
}

api_weather = requests.get(OWM_endpoint, params=parameters)
data = api_weather.json()
temp = float(data["main"]["temp"])
formula_c = temp - 273.15
print(formula_c)

if formula_c > 10:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = 'Garmi Bohat hay abhi AC chalao :p',
        from_="+12564148011",
        to="+923491454232"
    )
    print(message.status)
