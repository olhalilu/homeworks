import datetime
import requests

class News:
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def publish(self, file_name):
        with open(file_name, 'a') as file:
            file.write(f"News: {self.text}, City: {self.city}, Date: {self.date}\n")

class Adv:
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = expiration_date

    def days_left(self):
        today = datetime.datetime.now().date()
        days_left = (self.expiration_date - today).days
        return days_left

    def pub(self, file_name):
        with open(file_name, 'a') as file:
            file.write(f"Privat Ad: {self.text}, Expiration Date: {self.expiration_date}, Days Left: {self.days_left()}\n")

class Unique:
    def __init__(self, text, custom_info,city):
        self.text = text
        self.custom_info = custom_info
        self.city = city

    def get_weather(self):
        api_key = "ebf4f6a4e9877db728ff685028e38dbb"
        base_url = "https://api.openweathermap.org/data/2.5/weather"

        # Параметры запроса
        params = {
            "q": self.city,
            "appid": api_key,
            "units": "metric"  # Для получения температуры в градусах Цельсия
        }

        # GET-запрос
        response = requests.get(base_url, params=params)
        feel=" "
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            if temp<=15:
                feel = "it's very cold brrrr"
            else:
                feel = "it's warm outside=)"
        else:
            print(f"Ошибка: {response.status_code}, {response.text}")
        return weather, temp, feel



    def publish(self, file_name):
        # Implement your unique publishing rules here
        weather_info = self.get_weather()
        weather,temp,feel = weather_info
        with open(file_name, 'a') as file:
            file.write(f"Custom: {self.text}, Custom Info: {self.custom_info} weather in city {self.city}:{weather},{temp},{feel}\n")




def main():
    while True:
        print("Select the type of data you want to add:")
        print("1. News")
        print("2. Adv")
        print("3. Unique")
        choice = input("Enter your choice: ")

        if choice.lower() == 'news':
            text = input("Enter news text: ")
            city = input("Enter city: ")
            news_item = News(text, city)
            news_item.publish("news_feed.txt")
        elif choice.lower()  == 'adv':
            text = input("Enter ad text: ")
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
            expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
            ad_item = Adv(text, expiration_date)
            ad_item.pub("news_feed.txt")
        elif choice.lower()  == 'unique':
            text = input("Enter custom item text: ")
            custom_info = input("Enter custom information: ")
            city = input("enter your city: ")
            custom_item = Unique(text, custom_info,city)
            custom_item.publish("news_feed.txt")

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()