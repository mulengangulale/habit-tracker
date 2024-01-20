import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

my_token = config.get("API", "token")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": my_token,
    "username": "mulengangulale",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)