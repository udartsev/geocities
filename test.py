from SimpleDump import dump, dd
import geocities

#############################
#   TESTS
#############################


location = getCity(name="Ryazan")
# location = getCity(address="Забайкальская 24, Рязань")
print(location)
# dd('asd')

osm_id = location['osm_id']

# display_name = location.raw['display_name']
# place_id = location.raw['place_id']
# osm_id = location.raw['osm_id']

# print("display_name: " + str(display_name))
# print("place_id: " + str(place_id))
# print("osm_id: " + str(osm_id))

polygons = getPolygons(osm_id=osm_id)
print(polygons)


dd("exit")
