import requests
import json
from datetime import datetime


response = requests.get('https://66095c000f324a9a28832d7e.mockapi.io/users')
data = response.json()
new_user = {
    "name": "Robert Epicentre",
    "avatar": "My_photo.jpg",
    "state": "1000000000000000000000000000",
    "birth": "0000-00-00T00:00:00.586Z",
}


def find_name(data):
    for user in data:
        if user["name"] == "Wilson VonRueden":
            return user["id"]


def general_state(data):
    state = 0.00
    for user in data:
        if int(user["id"]) >= 77:
            return round(state, 2)
        else:
            state += float(user["state"])


def create_user(new_user):
    response_local = requests.post('https://66095c000f324a9a28832d7e.mockapi.io/users', json=new_user)
    return response_local.json()


def find_old_user(data):
    birth_day = []
    for user in data:
        birth_day.append(user["birth"].split("T")[0])
    for user in data:
        if user["birth"] == min(birth_day):
            return user["name"]


def find_poorest_user(data):
    min_state = []
    for user in data:
        min_state.append(float(user["state"]))
    for user in data:
        if user["state"] == str(min(min_state)):
            return user["name"]


def count_april(data):
    count = 0
    for user in data:
        if user["birth"].split("-")[1] == "04":
            count += 1
    return count


find_name(data)
general_state(data)
create_user(new_user)
find_old_user(data)
find_poorest_user(data)
count_april(data)
