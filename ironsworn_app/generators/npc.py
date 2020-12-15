import random
import os
import csv

from generators.table_handler import random_table_handler


class NPC():

    def __init__(self):

        self.npc_name = random_table_handler("npc_names", random.randint(1, 200))
        self.npc_desc_001 = random_table_handler("npc_descriptors", random.randint(1, 100))
        self.npc_desc_002 = random_table_handler("npc_descriptors", random.randint(1, 100))
        self.npc_desc_003 = random_table_handler("npc_descriptors", random.randint(1, 100))
        self.npc_role = random_table_handler("npc_role", random.randint(1, 100))
        self.npc_goal = random_table_handler("npc_goal", random.randint(1, 100))
        self.npc_stance = random_table_handler("npc_stance", random.randint(1, 10))
