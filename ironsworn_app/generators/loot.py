import random
import os
import csv

from generators.table_handler import random_table_handler

class Loot():

    def __init__(self):
        pass

    def generate_loot(self):

        loot_output = random_table_handler("loots", random.randint(1, 8))

        output = "[LOOT] \n{loot_output} \n".format(**locals())

        return output

