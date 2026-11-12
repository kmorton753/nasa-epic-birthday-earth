import os
from datetime import date, datetime

import requests


def retrieve_epic_photos(api_key, photo_date):
    endpoint_url = f"https://api.nasa.gov/EPIC/api/natural/date/{photo_date}"
    params = {"api_key": "DEMO_KEY"}

    response = requests.get(endpoint_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Data not received. Status code: {response.status_code}")
        return None

def build_image_ur1(photo):
  day = photo["date"].split(" ")[0]
  year, month, dd = day.split("-")
  return (
      f"https://epic.gsfc.nasa.gov/archive/natural/"
      f"{year}/{month}/{dd}/png/{photo['image']}.png"
  )

def ask_for_birthday():
  while True:
    text = input("Enter your birthday (YYYY-MM-DD), 2015 or later):").strip()

    try:
        birthday = datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        print("Please use the format YYYY-MM-DD.\n")
        continue

    if birthday.year < 2015:
      print("Epic photos start in 2015, so please enter 2015 or later.\n")
      continue

    if birthday > date.today():
      print("That date is in the future. Please try again.\n")
      continue

    return birthday.isoformat()


if __name__ == "__main__":
    photos = retrieve_epic_photos("DEMO_KEY", "2016-03-08")
    birthday = ask_for_birthday()
    
    if photos:
        print(f"Photos on this date: {len(photos)}")
        print()
        for key, value in photos[0].items():
            print(f"{key}: {value}")
        print()
        print("First image:", build_image_ur1(photos[0]))
    else:
        print("No photos for this date.")
