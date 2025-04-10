import os
import datetime
import requests
import csv
import string
import json
import xml.etree.ElementTree as ET
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

    def publish(self, file_name):
        with open(file_name, 'a') as file:
            file.write(
                f"Private Ad: {self.text}, Expiration Date: {self.expiration_date}, Days Left: {self.days_left()}\n"
            )


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
            feel = "Its warm outside" if temp > 15 else "Its very cold, brrr!"
        else:
            print(f"Error: {response.status_code}, {response.text}")
            weather, temp, feel = "N/A", "N/A", "Unable to fetch weather data"

        return weather, temp, feel

    def publish(self, file_name):
        weather_info = self.get_weather()
        weather, temp, feel = weather_info
        with open(file_name, 'a') as file:
            file.write(f"Custom: {self.text}, Weather in city {self.city}: {weather}, {temp}°C, {feel}\n")

#added json file processing
class JSONProcessor:
    def __init__(self, json_file_path="input_file.json", output_file="news_feed.txt"):
        self.json_file_path = json_file_path
        self.output_file = output_file

    def process_json_record(self, record):
        try:
            record_type = normalize_sentence(record["type"].strip())
            text = normalize_sentence(record["text"].strip())
            third_part = normalize_sentence(record["third_part"].strip())

            if record_type == "news":
                city = third_part
                news_item = News(text, city)
                news_item.publish(self.output_file)
            elif record_type == "adv":
                try:
                    expiration_date = datetime.datetime.strptime(third_part, "%Y-%m-%d").date()
                    ad_item = Adv(text, expiration_date)
                    ad_item.publish(self.output_file)
                except ValueError:
                    print(f"Invalid date format in record: {third_part}")
            elif record_type == "unique":
                city = third_part
                unique_item = Unique(text, city)
                unique_item.publish(self.output_file)
            else:
                print(f"Unknown record type: {record_type}")
        except KeyError as e:
            print(f"Invalid record format, missing key: {str(e)}")

    def process_json_file(self):
        try:
            with open(self.json_file_path, "r") as file:
                records = json.load(file)

                if isinstance(records, dict):
                    self.process_json_record(records)
                elif isinstance(records, list):
                    for record in records:
                        self.process_json_record(record)
                else:
                    print("Invalid JSON format: expected a dictionary or list of dictionaries.")

            #os.remove(self.json_file_path)
        except FileNotFoundError:
            print(f"Error: The file '{self.json_file_path}' was not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
        except Exception as e:
            print(f"An error occurred while processing the JSON file: {str(e)}")

#added XML file processing
class xmlProcessor:
    def __init__(self, xml_file_path="input_xml.xml", output_file="news_feed.txt"):
        self.xml_file_path = xml_file_path
        self.output_file = output_file

    def process_xml_file(self):
        try:
            tree = ET.parse(self.xml_file_path)
            root = tree.getroot()
            for record in root.findall('item'):
                self.process_xml_record(record)
            # os.remove(self.xml_file_path)
        except FileNotFoundError:
            print(f"Error: The file '{self.xml_file_path}' was not found.")
        except ET.ParseError as e:
            print(f"Error parsing XML: {str(e)}")
        except Exception as e:
            print(f"An error occurred while processing the XML file: {str(e)}")

    def process_xml_record(self, record):
        try:
            record_type = normalize_sentence(record.find("type").text.strip())
            text = normalize_sentence(record.find("text").text.strip())
            third_part = normalize_sentence(record.find("third_part").text.strip())

            if record_type == "news":
                city = third_part
                news_item = News(text, city)
                news_item.publish(self.output_file)
            elif record_type == "adv":
                try:
                    expiration_date = datetime.datetime.strptime(third_part, "%Y-%m-%d").date()
                    ad_item = Adv(text, expiration_date)
                    ad_item.publish(self.output_file)
                except ValueError:
                    print(f"Invalid date format in record: {third_part}")
            elif record_type == "unique":
                city = third_part
                unique_item = Unique(text, city)
                unique_item.publish(self.output_file)
            else:
                print(f"Unknown record type: {record_type}")
        except AttributeError as e:
            print(f"Invalid record format, missing element: {str(e)}")
        except Exception as e:
            print(f"An error occurred while processing the XML record: {str(e)}")


class FileProcessor:
    def __init__(self, file_path="input.txt", output_file="news_feed.txt"):
        self.file_path = file_path
        self.output_file = output_file

    def count_alpha_words_and_letters(self):
        try:
            with open(self.output_file, 'r') as file:
                content = file.read()
                translator = str.maketrans('', '', string.punctuation)
                cleaned_content = content.translate(translator)
                words = cleaned_content.split()
                alpha_words = [word for word in words if word.isalpha()]
                total_word_count = len(alpha_words)
                all_letters = ''.join(alpha_words)
                total_letter_count = len(all_letters)

                with open("word_count.csv", "w", newline='') as word_file:
                    writer = csv.writer(word_file)
                    writer.writerow(["col1", "col2"])
                    writer.writerow(["Total number of words: ", total_word_count])

                print(f"Word counts have been saved to 'word_count.csv'")

                with open("letter_count.csv", "w", newline='') as word_file:
                    writer = csv.writer(word_file)
                    writer.writerow(["col1", "col2"])
                    writer.writerow(["Total number of letters: ", total_letter_count])

                print(f"Letter counts have been saved to 'word_count.csv'")

        except FileNotFoundError:
            print(f"Error: The file '{self.output_file}' was not found.")
        except Exception as e:
            print(f"An error occurred while counting words and letters: {str(e)}")

    def process_record(self, record):
        if len(record) == 1:
            parts = record[0].split(",")
            if len(parts) < 3:
                print(f"Invalid record format: {record[0]}")
                return

            record_type = normalize_sentence(parts[0].strip())
            text = normalize_sentence(parts[1].strip())
            third_part = normalize_sentence(parts[2].strip())

        elif len(record) == 3:
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
                ad_item.publish(self.output_file)
            except ValueError:
                print(f"Invalid date format in record: {third_part}")
        elif record_type == "unique":
            city = third_part
            unique_item = Unique(text, city)
            unique_item.publish(self.output_file)
        else:
            print(f"Unknown record type: {record_type}")

    def process_file(self):
        try:
            with open(self.file_path, "r") as file:
                lines = []
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    lines.append(line)
                    if len(lines) == 3:
                        self.process_record(lines)
                        lines = []
                    elif len(lines) == 1 and "," in line:  #
                        self.process_record(lines)
                        lines = []

                if len(lines) > 0:
                    self.process_record(lines)

            #os.remove(self.file_path)
            self.count_alpha_words_and_letters()
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing the file: {str(e)}")

def main():
    input_type = input("Enter input type ('txt','json' or 'xml): ").strip().lower()
    if input_type == "txt":
        file_path = input("Enter file path or press Enter to use default (input.txt): ").strip() or "input.txt"
        processor = FileProcessor(file_path=file_path)
        processor.process_file()
    elif input_type == "json":
        json_file_path = input(
            "Enter JSON file path or press Enter to use default (input_file.json): ").strip() or "input_file.json"
        json_processor = JSONProcessor(json_file_path=json_file_path)
        json_processor.process_json_file()
    elif input_type == "xml":
        xml_file_path = input("Enter XML file path or press Enter to use default (input_xml.xml): ").strip() or "input_xml.xml"
        xml_processor = xmlProcessor(xml_file_path=xml_file_path)
        xml_processor.process_xml_file()
    else:
        print("Invalid input type. Please enter 'txt' or 'json'.")


if __name__ == "__main__":
    main()