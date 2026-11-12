# Nasa-epic-birthday-earth

Program asks for your date and uses NASA's EPIC data to show you how my photos of Earth were taken that day.

## How it works
ask_for_birthday: asks for a date (YYYY-MM-DD, 2015 or later) and keeps asking until it is valid
get_epic_photos: requests the photos for that date from the EPIC API and returns a list of dictionaries
build_image_ur1: uses the "date: and "image" keys from one photo to build the link to the photo
show_photo_detail: prints every key and value for one photo, then its image link
show_results: "No photos for this date."If there is no data, otherwise shows the photo count and the first photo
main: runs the steps in order

## How to run
1. Install requests: pip install requests
2. Run: python epic_birthday_earth.py
3. Uses "DEMO_KEY" by default. Swap in your own key
   from api.nasa.gov for higher rate limits.

## Built with
Python, requests and the NASA EPIC API
