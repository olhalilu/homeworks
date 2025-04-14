
from geopy.geocoders import Nominatim
from geopy.distance import geodesic




class Cities:
    def __init__(self, city_a, city_b):
        self.city_a = city_a
        self.city_b = city_b
        self.geolocator = Nominatim(user_agent="city_distance_app")

    def city_location(self):
        self.location_a = self.geolocator.geocode(self.city_a)
        self.location_b = self.geolocator.geocode(self.city_b)
        self.coord_a = (self.location_a.latitude, self.location_a.longitude)
        self.coord_b = (self.location_b.latitude, self.location_b.longitude)



    def city_distance(self):
        distance = geodesic(self.coord_a, self.coord_b).kilometers
        return distance


def main():
    city_a = input('enter city A: ')
    city_b = input('enter city B: ')

    try:
        city_item = Cities(city_a, city_b)
        city_item.city_location()
        distance = city_item.city_distance()
        print(f"distance between {city_a} and {city_b}: {distance:.2f} km")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"error: {e}")




if __name__ == "__main__":
    main()