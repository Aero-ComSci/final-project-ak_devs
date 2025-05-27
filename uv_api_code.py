import requests

API_KEY = "openuv-2l1xppormb6sbqw6-io"
# User inputs location, lat and lon pulled from dict, split at space, and converted to float.
LATITUDE = 37.7749
LONGITUDE = -122.4194


url = f"https://api.openuv.io/api/v1/uv?lat={LATITUDE}&lng={LONGITUDE}"

headers = {
    "x-access-token": API_KEY
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    uv_index = data['uv']
    print(f"The UV index for {LATITUDE}, {LONGITUDE} is: {uv_index}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")