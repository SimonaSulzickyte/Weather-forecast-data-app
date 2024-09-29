import requests
from datetime import datetime

with open('API.txt', 'r') as file:
    API_KEY = file.read() 

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

def format_date(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return dt.strftime("%a, %b %d %H:%M")


if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3))