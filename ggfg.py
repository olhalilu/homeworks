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



    def city_distance(self,location_a,location_b):
        distance = geodesic(self.coord_a, self.coord_b).kilometers

a = Cities("Chicago","miami")
b = a.city_location()

print(a)
print(b)

#
# def main():
#         city_a = input('please enter city A: ')
#         city_b = input('please enter city B: ')
#         cities = Cities(city_a,city_b)
#         loc = cities.city_location()
#         print(loc)
#
#
#
# if __name__ == "__main__":
#     main()