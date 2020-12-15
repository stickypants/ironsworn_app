import random
import os
import csv

from generators.table_handler import random_table_handler


class Settlement():

    def __init__(self):

        name_prefix = random_table_handler("settlement_prefix", random.randint(1, 100))
        name_sufix = random_table_handler("settlement_sufix", random.randint(1, 100))

        self.stl_name = name_prefix + name_sufix
        self.stl_governement = random_table_handler("settlement_governement", random.randint(1, 100))
        self.stl_known_for = random_table_handler("settlement_known_for", random.randint(1, 20))
        self.stl_trait = random_table_handler("settlement_traits", random.randint(1, 20))
        self.stl_trouble = random_table_handler("settlement_trouble", random.randint(1, 20))

    def generate_building(self):

        dice = random.randint(1, 20)

        if dice >= 1 and dice <= 10:
            output = self.generate_residence()
        if dice >= 11 and dice <= 12:
            output = self.generate_religious()
        if dice >= 13 and dice <= 15:
            output = self.generate_tavern()
        if dice >= 16 and dice <= 17:
            output = self.generate_warehouse()
        if dice >= 18 and dice <= 20:
            output = self.generate_shop()

        return output

    def generate_residence(self):

        residence_output = random_table_handler("residence", random.randint(1, 20))
        output = "[BUILDING - RESIDENCE] \n{residence_output} \n".format(**locals())

        return output

    def generate_religious(self):

        religious_output = random_table_handler("religious", random.randint(1, 20))
        output = "[BUILDING - RELIGIOUS] \n{religious_output} \n".format(**locals())

        return output

    def generate_tavern(self):

        tavern_type_output = random_table_handler("tavern", random.randint(1, 20))
        tavern_name_prefix = random_table_handler("travern_prefix", random.randint(1, 20))
        tavern_name_sufix = random_table_handler("travern_sufix", random.randint(1, 20))
        tavern_name = tavern_name_prefix + " " + tavern_name_sufix

        output = "[BUILDING - TARVERN] \n{tavern_type_output}\n{tavern_name} \n".format(**locals())

        return output

    def generate_warehouse(self):

        warehouse_output = random_table_handler("warehouse", random.randint(1, 20))
        output = "[BUILDING - WAREHOUSE] \n{warehouse_output} \n".format(**locals())

        return output

    def generate_shop(self):

        shop_output = random_table_handler("shop", random.randint(1, 20))
        output = "[BUILDING - SHOP] \n{shop_output} \n".format(**locals())

        return output



