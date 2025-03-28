import os
import datetime
import requests
from homework3 import normalize_sentence


class News:
    def __init__(self, text, city):
        self.text = normalize_sentence(text)
        self.city = normalize_sentence(city)
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def publish(self, file_name):
        with open(file_name, 'a') as file:
            file.write(f"News: {self.text}, City: {self.city}, Date: {self.date}\n")


class Adv:
    def __init__(self, text, expiration_date):
        self.text = normalize_sentence(text)
        self.expiration_date = expiration_date

    def days_left(self):
        today = datetime.datetime.now().date()
        days_left = (self.expiration_date - today).days
        return days_left

    def pub(self, file_name):
        with open(file_name, 'a') as file:
            file.write(
                f"Privat Ad: {self.text}, Expiration Date: {self.expiration_date}, Days Left: {self.days_left()}\n")


class Unique:
    def __init__(self, text, city):
        self.text = normalize_sentence(text)
        self.city = normalize_sentence(city)

    def get_weather(self):
        api_key = "ebf4f6a4e9877db728ff685028e38dbb"
        base_url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": self.city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(base_url, params=params)
        feel = " "
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feel = "it's warm outside=)" if temp > 15 else "it's very cold brrrr"
        else:
            print(f"Error: {response.status_code}, {response.text}")
        return weather, temp, feel

    def publish(self, file_name):
        weather_info = self.get_weather()
        weather, temp, feel = weather_info
        with open(file_name, 'a') as file:
            file.write(f"Custom: {self.text}, Weather in city {self.city}: {weather}, {temp}, {feel}\n")


class FileProcessor:
    def __init__(self, file_path="input.txt", output_file="news_feed.txt"):
        self.file_path = file_path
        self.output_file = output_file

    def process_record(self, record):

        if len(record) == 1:  # if 1 row
            parts = record[0].split(",")
            if len(parts) < 3:
                print(f"Invalid record format: {record[0]}")
                return

            record_type = normalize_sentence(parts[0].strip())
            text = normalize_sentence(parts[1].strip())
            third_part = normalize_sentence(parts[2].strip())

        elif len(record) == 3:  # if 3  rows
            record_type = normalize_sentence(record[0].strip())
            text = normalize_sentence(record[1].strip())
            third_part = normalize_sentence(record[2].strip())
        else:
            print("Invalid record format. Record must be a single line or three lines.")
            return

        if record_type == "news":
            city = third_part
            news_item = News(text, city)
            news_item.publish(self.output_file)
        elif record_type == "adv":
            try:
                expiration_date = datetime.datetime.strptime(third_part, "%Y-%m-%d").date()
                ad_item = Adv(text, expiration_date)
                ad_item.pub(self.output_file)
            except ValueError:
                print(f"Invalid date format in record: {third_part}")
        elif record_type == "unique":
            city = third_part
            unique_item = Unique(text, city)
            unique_item.publish(self.output_file)
        else:
            print(f"Unknown record type: {record_type}")

    def process_file(self):
        """
        Читает файл и обрабатывает записи.
        """
        try:
            with open(self.file_path, "r") as file:
                lines = []
                for line in file:
                    line = line.strip()
                    if not line:  # skip empty rows
                        continue

                    lines.append(line)
                    if len(lines) == 3:
                        self.process_record(lines)
                        lines = []
                    elif len(lines) == 1 and "," in line:
                        self.process_record(lines)
                        lines = []

                if len(lines) > 0:
                    self.process_record(lines)

            # delete file
            os.remove(self.file_path)
            print(f"Records have been saved to {self.output_file} and the file '{self.file_path}' has been deleted.")
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing the file: {str(e)}")


def main():
    """
    Запускает обработку данных из файла.
    """
    file_path = input("Enter file path or press Enter to use default (input.txt): ").strip() or "input.txt"
    processor = FileProcessor(file_path=file_path)
    processor.process_file()


if __name__ == "__main__":
    main()