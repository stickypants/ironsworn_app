import random
import os
import csv

from generators.table_handler import random_table_handler

class Waypoint():

    def __init__(self):
        pass

    def generate_waypoint(self):

        location = random.randint(1, 100)
        location_desc_001 = random.randint(1, 100)
        location_desc_002 = random.randint(1, 100)

        location_output = random_table_handler("locations", location)
        location_desc_001_output = random_table_handler("locations_descriptors", location_desc_001)
        location_desc_002_output = random_table_handler("locations_descriptors", location_desc_002)

        output = "[WAYPOINT] \nAfter a day's travel, you have arrived at a \nLocation : {location_output} \n" \
                 "Location Descriptor : {location_desc_001_output} {location_desc_002_output} \n".format(**locals())

        return output

if __name__ == "__main__":
    w = Waypoint()
    out = w.generate_waypoint()
    print(out)